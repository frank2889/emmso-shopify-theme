"""
Analysis Memory System for EMMSO AI
===================================

Maintains memory of analysis iterations, findings, and trends
to enable progressive improvement and avoid regression.
"""

import os
import json
from typing import Dict, List, Any, Optional
from datetime import datetime

class AnalysisMemory:
    """Memory system for storing and retrieving analysis data."""
    
    def __init__(self):
        """Initialize memory system."""
        self.memory_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'data',
            'analysis_memory.json'
        )
        
        # Ensure data directory exists
        os.makedirs(os.path.dirname(self.memory_file), exist_ok=True)
        
        self.memory = self._load_memory()
    
    def _load_memory(self) -> Dict[str, Any]:
        """Load existing memory from file."""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not load memory file: {e}")
        
        # Return default memory structure
        return {
            'sessions': [],
            'analyst_history': {},
            'trends': {},
            'recommendations_status': {},
            'last_updated': None
        }
    
    def _save_memory(self):
        """Save memory to file."""
        try:
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(self.memory, f, indent=2, default=str)
        except IOError as e:
            print(f"Warning: Could not save memory file: {e}")
    
    def start_new_session(self) -> str:
        """Start a new analysis session."""
        session_id = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        session = {
            'session_id': session_id,
            'start_time': datetime.now().isoformat(),
            'iterations': [],
            'status': 'active'
        }
        
        self.memory['sessions'].append(session)
        self.memory['last_updated'] = datetime.now().isoformat()
        self._save_memory()
        
        return session_id
    
    def store_iteration(self, iteration: int, results: Dict[str, Any]):
        """Store results from a single iteration."""
        if not self.memory['sessions']:
            self.start_new_session()
        
        current_session = self.memory['sessions'][-1]
        
        # Store iteration data
        iteration_data = {
            'iteration': iteration,
            'timestamp': datetime.now().isoformat(),
            'scores': results.get('analyst_scores', {}),
            'findings': results.get('findings', {}),
            'summary': self._summarize_iteration(results)
        }
        
        current_session['iterations'].append(iteration_data)
        
        # Update analyst history
        for analyst_name, score in results.get('analyst_scores', {}).items():
            if analyst_name not in self.memory['analyst_history']:
                self.memory['analyst_history'][analyst_name] = []
            
            self.memory['analyst_history'][analyst_name].append({
                'iteration': iteration,
                'session': current_session['session_id'],
                'score': score,
                'timestamp': datetime.now().isoformat()
            })
        
        # Update trends
        self._update_trends(results.get('analyst_scores', {}))
        
        self._save_memory()
    
    def get_previous_findings(self, analyst_name: str) -> Dict[str, Any]:
        """Get previous findings for a specific analyst."""
        history = self.memory['analyst_history'].get(analyst_name, [])
        
        if not history:
            return {}
        
        # Get last 3 findings
        recent_history = history[-3:]
        
        return {
            'recent_scores': [h['score'] for h in recent_history],
            'trend': self._calculate_trend([h['score'] for h in recent_history]),
            'last_score': recent_history[-1]['score'] if recent_history else 0,
            'session_count': len(set(h['session'] for h in history)),
            'total_iterations': len(history)
        }
    
    def get_session_summary(self, session_id: Optional[str] = None) -> Dict[str, Any]:
        """Get summary of a specific session or the current one."""
        if session_id:
            session = next((s for s in self.memory['sessions'] if s['session_id'] == session_id), None)
        else:
            session = self.memory['sessions'][-1] if self.memory['sessions'] else None
        
        if not session:
            return {}
        
        iterations = session.get('iterations', [])
        if not iterations:
            return {'session_id': session.get('session_id'), 'status': 'no_data'}
        
        # Calculate summary statistics
        final_scores = {}
        trends = {}
        
        for analyst_name in set().union(*(it['scores'].keys() for it in iterations)):
            scores = [it['scores'].get(analyst_name, 0) for it in iterations]
            final_scores[analyst_name] = scores[-1] if scores else 0
            trends[analyst_name] = scores[-1] - scores[0] if len(scores) > 1 else 0
        
        return {
            'session_id': session['session_id'],
            'start_time': session['start_time'],
            'total_iterations': len(iterations),
            'final_scores': final_scores,
            'trends': trends,
            'avg_score': sum(final_scores.values()) / len(final_scores) if final_scores else 0,
            'status': session.get('status', 'unknown')
        }
    
    def get_global_trends(self) -> Dict[str, Any]:
        """Get global trends across all sessions."""
        trends = {}
        
        for analyst_name, history in self.memory['analyst_history'].items():
            if len(history) < 2:
                continue
            
            scores = [h['score'] for h in history]
            trends[analyst_name] = {
                'current_score': scores[-1],
                'best_score': max(scores),
                'worst_score': min(scores),
                'avg_score': sum(scores) / len(scores),
                'total_change': scores[-1] - scores[0],
                'recent_trend': self._calculate_trend(scores[-5:]) if len(scores) >= 5 else 'insufficient_data'
            }
        
        return trends
    
    def mark_recommendation_implemented(self, recommendation_id: str, notes: str = ""):
        """Mark a recommendation as implemented."""
        self.memory['recommendations_status'][recommendation_id] = {
            'status': 'implemented',
            'timestamp': datetime.now().isoformat(),
            'notes': notes
        }
        self._save_memory()
    
    def _summarize_iteration(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Create a summary of iteration results."""
        scores = results.get('analyst_scores', {})
        
        return {
            'avg_score': sum(scores.values()) / len(scores) if scores else 0,
            'critical_count': sum(1 for score in scores.values() if score < 30),
            'passing_count': sum(1 for score in scores.values() if score >= 70),
            'lowest_scorer': min(scores.items(), key=lambda x: x[1]) if scores else None,
            'highest_scorer': max(scores.items(), key=lambda x: x[1]) if scores else None
        }
    
    def _update_trends(self, current_scores: Dict[str, float]):
        """Update trend information."""
        for analyst_name, score in current_scores.items():
            history = self.memory['analyst_history'].get(analyst_name, [])
            
            if len(history) >= 2:
                recent_scores = [h['score'] for h in history[-5:]]  # Last 5 scores
                trend = self._calculate_trend(recent_scores)
                
                self.memory['trends'][analyst_name] = {
                    'direction': trend,
                    'last_updated': datetime.now().isoformat(),
                    'score_change': score - history[-2]['score'] if len(history) >= 2 else 0
                }
    
    def _calculate_trend(self, scores: List[float]) -> str:
        """Calculate trend direction from a list of scores."""
        if len(scores) < 2:
            return 'insufficient_data'
        
        # Simple trend calculation
        first_half = scores[:len(scores)//2]
        second_half = scores[len(scores)//2:]
        
        avg_first = sum(first_half) / len(first_half)
        avg_second = sum(second_half) / len(second_half)
        
        diff = avg_second - avg_first
        
        if diff > 5:
            return 'improving'
        elif diff < -5:
            return 'declining'
        else:
            return 'stable'
    
    def export_data(self, format: str = 'json') -> str:
        """Export memory data for analysis."""
        if format == 'json':
            return json.dumps(self.memory, indent=2, default=str)
        else:
            raise ValueError(f"Unsupported export format: {format}")
    
    def cleanup_old_sessions(self, days_to_keep: int = 30):
        """Remove old sessions to keep memory file manageable."""
        cutoff_date = datetime.now().timestamp() - (days_to_keep * 24 * 60 * 60)
        
        sessions_to_keep = []
        for session in self.memory['sessions']:
            session_date = datetime.fromisoformat(session['start_time']).timestamp()
            if session_date > cutoff_date:
                sessions_to_keep.append(session)
        
        removed_count = len(self.memory['sessions']) - len(sessions_to_keep)
        self.memory['sessions'] = sessions_to_keep
        
        if removed_count > 0:
            print(f"Cleaned up {removed_count} old sessions")
            self._save_memory()
        
        return removed_count