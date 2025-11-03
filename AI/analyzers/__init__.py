"""# EMMSO AI analyzers
EMMSO AI Analyzers Module
=========================

Collection of specialized AI analysts for comprehensive Shopify theme analysis.
"""

from .sarah import SarahSEOAnalyst
from .eva import EvaAnalyticsAnalyst
from .mike import MikeConversionAnalyst

# Placeholder imports for other analysts (to be implemented)
try:
    from .marcus import MarcusPerformanceAnalyst
except ImportError:
    MarcusPerformanceAnalyst = None

try:
    from .jessica import JessicaUXAnalyst
except ImportError:
    JessicaUXAnalyst = None

try:
    from .rachel import RachelContentAnalyst
except ImportError:
    RachelContentAnalyst = None

try:
    from .alex import AlexShopifyAnalyst
except ImportError:
    AlexShopifyAnalyst = None

try:
    from .nora import NoraVisualDesignAnalyst
except ImportError:
    NoraVisualDesignAnalyst = None

__all__ = [
    'SarahSEOAnalyst',
    'EvaAnalyticsAnalyst', 
    'MikeConversionAnalyst',
    'MarcusPerformanceAnalyst',
    'JessicaUXAnalyst',
    'RachelContentAnalyst',
    'AlexShopifyAnalyst',
    'NoraVisualDesignAnalyst'
]