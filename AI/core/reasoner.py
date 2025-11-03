"""
Reasoning Engine for EMMSO AI System
====================================

Provides intelligent reasoning capabilities for:
- Cross-analyst correlation analysis
- Priority setting and recommendation ranking
- Conflict resolution between analyst findings
- Strategic decision making
"""

from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import statistics

class ReasoningEngine:
    """Advanced reasoning engine for AI analysis coordination."""
    
    def __init__(self):
        """Initialize the reasoning engine."""
        self.priority_weights = {
            'conversion_impact': 0.3,    # How much it affects conversions
            'user_experience': 0.25,     # Impact on user experience
            'technical_difficulty': 0.2, # How hard it is to implement
            'seo_impact': 0.15,         # SEO implications
            'brand_impact': 0.1         # Brand/visual impact
        }
        
        self.analyst_expertise = {
            'sarah': ['seo', 'content_quality', 'technical_seo'],
            'marcus': ['performance', 'technical_optimization', 'loading_speed'],
            'jessica': ['user_experience', 'accessibility', 'usability'],
            'rachel': ['content_strategy', 'messaging', 'copywriting'],
            'alex': ['shopify_optimization', 'ecommerce_features', 'conversions'],
            'eva': ['analytics', 'data_interpretation', 'trends'],
            'mike': ['conversion_optimization', 'sales_funnel', 'cro'],
            'nora': ['visual_design', 'branding', 'aesthetics']
        }
    
    def analyze_findings_correlation(self, findings: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze correlations between different analyst findings.
        
        Args:
            findings: Dict of analyst findings
            
        Returns:
            Correlation analysis results
        """
        correlations = {}
        conflicts = []
        synergies = []
        
        # Find correlations between analyst scores
        scores = {name: finding.get('score', 0) for name, finding in findings.items()}
        
        # Identify strong correlations
        for analyst1, score1 in scores.items():
            for analyst2, score2 in scores.items():
                if analyst1 != analyst2:
                    correlation = self._calculate_correlation(analyst1, analyst2, score1, score2)
                    if abs(correlation) > 0.7:  # Strong correlation
                        correlations[f"{analyst1}_{analyst2}"] = correlation
        
        # Find conflicts (contradictory recommendations)
        conflicts = self._identify_conflicts(findings)
        
        # Find synergies (reinforcing recommendations)
        synergies = self._identify_synergies(findings)
        
        return {
            'score_correlations': correlations,
            'conflicts': conflicts,
            'synergies': synergies,
            'overall_coherence': self._calculate_coherence(scores)
        }
    
    def prioritize_recommendations(self, all_recommendations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Prioritize recommendations using intelligent reasoning.
        
        Args:
            all_recommendations: List of recommendations from all analysts
            
        Returns:
            Prioritized list of recommendations
        """
        scored_recommendations = []
        
        for rec in all_recommendations:
            priority_score = self._calculate_priority_score(rec)
            rec['priority_score'] = priority_score
            rec['reasoning'] = self._explain_priority(rec, priority_score)
            scored_recommendations.append(rec)
        
        # Sort by priority score (highest first)
        scored_recommendations.sort(key=lambda x: x['priority_score'], reverse=True)
        
        # Group into priority categories
        high_priority = [r for r in scored_recommendations if r['priority_score'] > 0.8]
        medium_priority = [r for r in scored_recommendations if 0.5 <= r['priority_score'] <= 0.8]
        low_priority = [r for r in scored_recommendations if r['priority_score'] < 0.5]
        
        return {
            'high_priority': high_priority,
            'medium_priority': medium_priority,
            'low_priority': low_priority,
            'total_count': len(scored_recommendations)
        }
    
    def resolve_conflicts(self, conflicts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Resolve conflicts between analyst recommendations.
        
        Args:
            conflicts: List of identified conflicts
            
        Returns:
            Conflict resolutions with reasoning
        """
        resolutions = []
        
        for conflict in conflicts:
            resolution = self._resolve_single_conflict(conflict)
            resolutions.append(resolution)
        
        return resolutions
    
    def generate_strategic_insights(self, analysis_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate strategic insights from analysis history.
        
        Args:
            analysis_history: Historical analysis data
            
        Returns:
            Strategic insights and recommendations
        """
        if len(analysis_history) < 2:
            return {'message': 'Insufficient data for strategic analysis'}
        
        # Analyze trends
        trends = self._analyze_trends(analysis_history)
        
        # Identify patterns
        patterns = self._identify_patterns(analysis_history)
        
        # Generate strategic recommendations
        strategic_recs = self._generate_strategic_recommendations(trends, patterns)
        
        return {
            'trends': trends,
            'patterns': patterns,
            'strategic_recommendations': strategic_recs,
            'confidence_level': self._calculate_confidence(analysis_history)
        }
    
    def _calculate_correlation(self, analyst1: str, analyst2: str, score1: float, score2: float) -> float:
        """Calculate correlation between two analysts based on expertise overlap."""
        
        # Get expertise overlap
        expertise1 = set(self.analyst_expertise.get(analyst1, []))
        expertise2 = set(self.analyst_expertise.get(analyst2, []))
        
        overlap = len(expertise1.intersection(expertise2))
        total_unique = len(expertise1.union(expertise2))
        
        expertise_similarity = overlap / total_unique if total_unique > 0 else 0
        
        # Score difference factor
        score_diff = abs(score1 - score2) / 100.0  # Normalize to 0-1
        score_similarity = 1 - score_diff
        
        # Combined correlation
        correlation = (expertise_similarity * 0.7) + (score_similarity * 0.3)
        
        return correlation
    
    def _identify_conflicts(self, findings: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify conflicts between analyst recommendations."""
        conflicts = []
        
        # Look for contradictory recommendations
        all_recs = []
        for analyst, finding in findings.items():
            recs = finding.get('recommendations', [])
            for rec in recs:
                rec['analyst'] = analyst
                all_recs.append(rec)
        
        # Check for contradictions
        for i, rec1 in enumerate(all_recs):
            for rec2 in all_recs[i+1:]:
                if self._are_conflicting(rec1, rec2):
                    conflicts.append({
                        'type': 'recommendation_conflict',
                        'analyst1': rec1['analyst'],
                        'analyst2': rec2['analyst'],
                        'recommendation1': rec1,
                        'recommendation2': rec2,
                        'severity': self._assess_conflict_severity(rec1, rec2)
                    })
        
        return conflicts
    
    def _identify_synergies(self, findings: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify synergistic recommendations that reinforce each other."""
        synergies = []
        
        all_recs = []
        for analyst, finding in findings.items():
            recs = finding.get('recommendations', [])
            for rec in recs:
                rec['analyst'] = analyst
                all_recs.append(rec)
        
        # Find synergistic recommendations
        for i, rec1 in enumerate(all_recs):
            for rec2 in all_recs[i+1:]:
                if self._are_synergistic(rec1, rec2):
                    synergies.append({
                        'type': 'recommendation_synergy',
                        'analysts': [rec1['analyst'], rec2['analyst']],
                        'recommendations': [rec1, rec2],
                        'synergy_strength': self._assess_synergy_strength(rec1, rec2),
                        'combined_impact': self._estimate_combined_impact(rec1, rec2)
                    })
        
        return synergies
    
    def _calculate_coherence(self, scores: Dict[str, float]) -> float:
        """Calculate overall coherence of analyst scores."""
        if len(scores) < 2:
            return 1.0
        
        score_values = list(scores.values())
        mean_score = statistics.mean(score_values)
        std_dev = statistics.stdev(score_values) if len(score_values) > 1 else 0
        
        # Coherence is higher when standard deviation is lower
        coherence = max(0, 1 - (std_dev / 100))  # Normalize by max possible std dev
        
        return coherence
    
    def _calculate_priority_score(self, recommendation: Dict[str, Any]) -> float:
        """Calculate priority score for a recommendation."""
        
        # Base score from stated priority
        priority_map = {'critical': 1.0, 'high': 0.8, 'medium': 0.6, 'low': 0.4}
        base_score = priority_map.get(recommendation.get('priority', 'medium'), 0.6)
        
        # Impact factor
        impact_map = {'high': 1.0, 'medium': 0.7, 'low': 0.4}
        impact_factor = impact_map.get(recommendation.get('impact', 'medium'), 0.7)
        
        # Difficulty factor (easier implementations get higher priority for quick wins)
        difficulty_map = {'easy': 1.0, 'medium': 0.8, 'hard': 0.6}
        difficulty_factor = difficulty_map.get(recommendation.get('difficulty', 'medium'), 0.8)
        
        # Analyst expertise weight (some analysts have higher weight for certain areas)
        analyst = recommendation.get('analyst', '')
        expertise_weight = self._get_analyst_weight(analyst, recommendation)
        
        # Calculate final score
        priority_score = (
            base_score * 0.4 +
            impact_factor * 0.3 +
            difficulty_factor * 0.2 +
            expertise_weight * 0.1
        )
        
        return min(1.0, priority_score)
    
    def _explain_priority(self, recommendation: Dict[str, Any], score: float) -> str:
        """Generate explanation for priority score."""
        
        explanations = []
        
        if score > 0.8:
            explanations.append("High priority due to significant impact potential")
        elif score > 0.6:
            explanations.append("Medium priority with good ROI")
        else:
            explanations.append("Lower priority, consider for future implementation")
        
        # Add specific reasoning based on recommendation attributes
        if recommendation.get('impact') == 'high':
            explanations.append("high user impact")
        
        if recommendation.get('difficulty') == 'easy':
            explanations.append("easy to implement")
        
        if recommendation.get('priority') == 'critical':
            explanations.append("marked as critical by analyst")
        
        return "; ".join(explanations)
    
    def _resolve_single_conflict(self, conflict: Dict[str, Any]) -> Dict[str, Any]:
        """Resolve a single conflict between recommendations."""
        
        rec1 = conflict['recommendation1']
        rec2 = conflict['recommendation2']
        
        # Determine which recommendation to prioritize
        score1 = self._calculate_priority_score(rec1)
        score2 = self._calculate_priority_score(rec2)
        
        if score1 > score2:
            chosen = rec1
            alternative = rec2
        else:
            chosen = rec2
            alternative = rec1
        
        return {
            'conflict_id': f"{conflict['analyst1']}_{conflict['analyst2']}",
            'resolution': 'prioritize_higher_impact',
            'chosen_recommendation': chosen,
            'alternative_approach': alternative,
            'reasoning': f"Prioritizing {chosen['analyst']}'s recommendation due to higher impact score",
            'suggested_compromise': self._suggest_compromise(rec1, rec2)
        }
    
    def _are_conflicting(self, rec1: Dict[str, Any], rec2: Dict[str, Any]) -> bool:
        """Check if two recommendations are conflicting."""
        
        # Simple conflict detection based on keywords
        conflicting_pairs = [
            (['remove', 'delete'], ['add', 'implement']),
            (['increase'], ['decrease', 'reduce']),
            (['simplify'], ['enhance', 'complex']),
        ]
        
        text1 = f"{rec1.get('title', '')} {rec1.get('description', '')}".lower()
        text2 = f"{rec2.get('title', '')} {rec2.get('description', '')}".lower()
        
        for conflict_group in conflicting_pairs:
            if (any(word in text1 for word in conflict_group[0]) and 
                any(word in text2 for word in conflict_group[1])):
                return True
            if (any(word in text1 for word in conflict_group[1]) and 
                any(word in text2 for word in conflict_group[0])):
                return True
        
        return False
    
    def _are_synergistic(self, rec1: Dict[str, Any], rec2: Dict[str, Any]) -> bool:
        """Check if two recommendations are synergistic."""
        
        # Look for synergistic keywords
        synergistic_keywords = [
            'optimization', 'performance', 'user experience', 'conversion',
            'accessibility', 'seo', 'loading', 'mobile', 'design'
        ]
        
        text1 = f"{rec1.get('title', '')} {rec1.get('description', '')}".lower()
        text2 = f"{rec2.get('title', '')} {rec2.get('description', '')}".lower()
        
        common_keywords = sum(1 for keyword in synergistic_keywords 
                            if keyword in text1 and keyword in text2)
        
        return common_keywords >= 2
    
    def _assess_conflict_severity(self, rec1: Dict[str, Any], rec2: Dict[str, Any]) -> str:
        """Assess the severity of a conflict between recommendations."""
        
        # High severity if both are high priority
        if (rec1.get('priority') in ['critical', 'high'] and 
            rec2.get('priority') in ['critical', 'high']):
            return 'high'
        
        # Medium severity if one is high priority
        if (rec1.get('priority') in ['critical', 'high'] or 
            rec2.get('priority') in ['critical', 'high']):
            return 'medium'
        
        return 'low'
    
    def _assess_synergy_strength(self, rec1: Dict[str, Any], rec2: Dict[str, Any]) -> float:
        """Assess the strength of synergy between recommendations."""
        
        # Simple scoring based on priority and impact alignment
        priority_score = 0.5
        if rec1.get('priority') == rec2.get('priority'):
            priority_score = 1.0
        
        impact_score = 0.5
        if rec1.get('impact') == rec2.get('impact'):
            impact_score = 1.0
        
        return (priority_score + impact_score) / 2
    
    def _estimate_combined_impact(self, rec1: Dict[str, Any], rec2: Dict[str, Any]) -> str:
        """Estimate the combined impact of synergistic recommendations."""
        
        impacts = [rec1.get('impact', 'medium'), rec2.get('impact', 'medium')]
        
        if 'high' in impacts:
            return 'very_high' if impacts.count('high') == 2 else 'high'
        elif 'medium' in impacts:
            return 'medium'
        else:
            return 'low'
    
    def _get_analyst_weight(self, analyst: str, recommendation: Dict[str, Any]) -> float:
        """Get weight for analyst based on their expertise relevance."""
        
        # Default weight
        base_weight = 0.5
        
        # Higher weight for analysts in their area of expertise
        expertise_areas = self.analyst_expertise.get(analyst, [])
        rec_text = f"{recommendation.get('title', '')} {recommendation.get('description', '')}".lower()
        
        relevance_score = sum(1 for area in expertise_areas if area.replace('_', ' ') in rec_text)
        
        return min(1.0, base_weight + (relevance_score * 0.2))
    
    def _analyze_trends(self, history: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze trends in historical data."""
        
        # Extract scores over time
        analyst_trends = {}
        
        for analyst in self.analyst_expertise.keys():
            scores = []
            for analysis in history:
                if 'analyst_scores' in analysis:
                    score = analysis['analyst_scores'].get(analyst, 0)
                    scores.append(score)
            
            if len(scores) > 1:
                trend = 'improving' if scores[-1] > scores[0] else 'declining'
                if abs(scores[-1] - scores[0]) < 5:
                    trend = 'stable'
                
                analyst_trends[analyst] = {
                    'trend': trend,
                    'change': scores[-1] - scores[0],
                    'current_score': scores[-1],
                    'best_score': max(scores),
                    'consistency': self._calculate_consistency(scores)
                }
        
        return analyst_trends
    
    def _identify_patterns(self, history: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identify patterns in analysis history."""
        
        patterns = []
        
        # Pattern: Consistent low performers
        for analysis in history[-3:]:  # Last 3 analyses
            scores = analysis.get('analyst_scores', {})
            low_performers = [name for name, score in scores.items() if score < 30]
            
            if len(low_performers) > 0:
                patterns.append({
                    'type': 'consistent_low_performance',
                    'analysts': low_performers,
                    'recommendation': 'Focus on fundamental issues in these areas'
                })
        
        # Pattern: Rapid improvement
        for analyst in self.analyst_expertise.keys():
            recent_scores = []
            for analysis in history[-5:]:
                if 'analyst_scores' in analysis:
                    score = analysis['analyst_scores'].get(analyst, 0)
                    recent_scores.append(score)
            
            if len(recent_scores) >= 3:
                improvement = recent_scores[-1] - recent_scores[0]
                if improvement > 20:  # 20+ point improvement
                    patterns.append({
                        'type': 'rapid_improvement',
                        'analyst': analyst,
                        'improvement': improvement,
                        'recommendation': f'Continue successful strategies for {analyst}'
                    })
        
        return patterns
    
    def _generate_strategic_recommendations(self, trends: Dict[str, Any], patterns: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate strategic recommendations based on trends and patterns."""
        
        strategic_recs = []
        
        # Based on trends
        declining_analysts = [name for name, data in trends.items() 
                            if data['trend'] == 'declining']
        
        if declining_analysts:
            strategic_recs.append({
                'type': 'trend_based',
                'title': 'Address declining performance areas',
                'description': f"Focus on {', '.join(declining_analysts)} which show declining trends",
                'priority': 'high',
                'timeframe': 'immediate'
            })
        
        # Based on patterns
        for pattern in patterns:
            if pattern['type'] == 'consistent_low_performance':
                strategic_recs.append({
                    'type': 'pattern_based',
                    'title': 'Fundamental improvements needed',
                    'description': f"Address core issues in {', '.join(pattern['analysts'])}",
                    'priority': 'critical',
                    'timeframe': 'immediate'
                })
        
        return strategic_recs
    
    def _calculate_confidence(self, history: List[Dict[str, Any]]) -> float:
        """Calculate confidence level in analysis based on data quality."""
        
        # More data points = higher confidence
        data_points = len(history)
        data_confidence = min(1.0, data_points / 10)  # Max confidence at 10+ data points
        
        # Consistency in results = higher confidence
        if data_points >= 3:
            recent_analyses = history[-3:]
            score_variations = []
            
            for analyst in self.analyst_expertise.keys():
                scores = [a.get('analyst_scores', {}).get(analyst, 0) for a in recent_analyses]
                if len(scores) > 1:
                    variation = max(scores) - min(scores)
                    score_variations.append(variation)
            
            avg_variation = sum(score_variations) / len(score_variations) if score_variations else 50
            consistency_confidence = max(0, 1 - (avg_variation / 100))
        else:
            consistency_confidence = 0.5
        
        return (data_confidence + consistency_confidence) / 2
    
    def _calculate_consistency(self, scores: List[float]) -> float:
        """Calculate consistency score for a series of values."""
        if len(scores) < 2:
            return 1.0
        
        variations = [abs(scores[i] - scores[i-1]) for i in range(1, len(scores))]
        avg_variation = sum(variations) / len(variations)
        
        # Lower variation = higher consistency
        return max(0, 1 - (avg_variation / 100))
    
    def _suggest_compromise(self, rec1: Dict[str, Any], rec2: Dict[str, Any]) -> str:
        """Suggest a compromise between conflicting recommendations."""
        
        return f"Consider implementing elements from both {rec1['analyst']} and {rec2['analyst']} approaches in phases"