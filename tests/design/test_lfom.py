from aguaclara.design.lfom import LFOM
from aguaclara.core.units import unit_registry as u

def test_lfom(lfom):
    assert lfom.width_stout(10*u.cm).to(u.m) == 0.002405154520928927*u.m
    assert lfom.n_rows == 10
    assert lfom.b_rows.to(u.m) == 0.03*u.m
    assert lfom.vel_critical.to(u.m/u.s) == 1.0294963872061624 * u.m/u.s
    assert lfom.area_pipe_min.to(u.m**2) == 0.043710692489286516 * u.m**2
    assert lfom.nom_diam_pipe.to(u.inch) == 10 * u.inch
    assert lfom.area_top_orifice.to(u.m**2) == 4.274071743928371e-05*u.m**2
    assert lfom.d_orifice_max.to(u.m) == 0.00737693510978969 * u.m
    assert lfom.orifice_diameter.to(u.m) == 0.00635*u.m
    assert lfom.drillbit_area.to(u.m**2) == 3.1669217443593606e-05*u.m**2
    assert lfom.n_orifices_per_row_max == 48