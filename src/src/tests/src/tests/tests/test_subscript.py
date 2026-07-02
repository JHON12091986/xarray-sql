import pytest
import xarray as xr
import xarray_sql as xql

def test_subscript_access():
    ds = xr.tutorial.open_dataset('air_temperature')
    ctx = xql.XarrayContext()
    ctx.from_dataset('air', ds, chunks=dict(time=100))
    
    # Prueba acceso por subíndice
    table = ctx["air"]
    assert table is not None

def test_chunks_property():
    ds = xr.tutorial.open_dataset('air_temperature')
    ctx = xql.XarrayContext()
    ctx.from_dataset('air', ds, chunks=dict(time=100))
    
    # Prueba propiedad chunks
    chunks = ctx["air"].chunks
    assert chunks is not None