"""# EMMSO AI analyzers
EMMSO AI Analyzers Module
=========================

Collection of specialized AI analysts for comprehensive Shopify theme analysis.
"""

from .sarah import SarahSEOAnalyst
# from .eva import EvaAnalyticsAnalyst  # Temporarily disabled - Google Analytics dependency
from .mike import MikeConversionAnalyst

# Placeholder imports for other analysts (to be implemented)
try:
    from .marcus import MarcusPerformanceAnalyst
except ImportError:
    MarcusPerformanceAnalyst = None

# Disabled due to Google Analytics dependency
# try:
#     from .jessica import JessicaUXAnalyst
# except ImportError:
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
    from .nora import NoraVisualAnalyst
except ImportError:
    NoraVisualAnalyst = None

try:
    from .vision import VisionAIAnalyst
except ImportError:
    VisionAIAnalyst = None

__all__ = [
    'SarahSEOAnalyst',
    'EvaAnalyticsAnalyst', 
    'MikeConversionAnalyst',
    'MarcusPerformanceAnalyst',
    'JessicaUXAnalyst',
    'RachelContentAnalyst',
    'AlexShopifyAnalyst',
    'NoraVisualDesignAnalyst',
    'VisionAIAnalyst'
]