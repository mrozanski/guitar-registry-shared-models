"""
Eddie Shared Models - Guitar Registry Data Structures

This package provides shared Pydantic models for guitar data structures,
ensuring consistency between data generation and validation systems.
"""

from .guitar_models import (
    # Core models
    Manufacturer,
    Model,
    IndividualGuitar,
    SourceAttribution,
    Specifications,
    Finish,
    
    # Composite models
    GuitarSubmission,
    BatchSubmission,
    
    # Enums
    ManufacturerStatus,
    ProductionType,
    SignificanceLevel,
    ConditionRating,
    SourceType,
    FinishRarity,
)

__version__ = "0.1.0"
__all__ = [
    "Manufacturer",
    "Model", 
    "IndividualGuitar",
    "SourceAttribution",
    "Specifications",
    "Finish",
    "GuitarSubmission",
    "BatchSubmission",
    "ManufacturerStatus",
    "ProductionType",
    "SignificanceLevel",
    "ConditionRating",
    "SourceType",
    "FinishRarity",
]
