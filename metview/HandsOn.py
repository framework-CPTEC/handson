import metview as mv

def build_layout():
    _Geographical_View_ = mv.geoview()
    _Page_ = mv.plot_page(
        top=0,
        bottom=100,
        left=0,
        right=100,
        view=_Geographical_View_
    )
    dw = mv.plot_superpage(
        layout_size="A4",
        layout_orientation="LANDSCAPE",
        custom_width=29.7,
        custom_height=21.0,
        pages=[_Page_]
    )
    return dw

# Downloads
Download1 = mv.download(url="https://dataserver.cptec.inpe.br/dataserver_modelos/wrf/ams_07km/brutos/2025/11/13/00/WRF_cpt_07KM_2025111300_2025111301.grib2")
Download2 = mv.download(url="https://ftp.cptec.inpe.br/modelos/tempo/CRNG/techtalk/bufr/202502150000_temp.bufr")
Download3 = mv.download(url="https://ftp.cptec.inpe.br/modelos/tempo/CRNG/techtalk/bufr/202502150000_metar.bufr")

# Estilo de contorno
Contouring = mv.mcont(
    legend="ON",
    contour_line_colour_rainbow="ON",
    contour_highlight="OFF",
    contour_shade="ON",
    contour_shade_method="AREA_FILL"
)


# Layout
dw = build_layout()

# Plot todos juntos
mv.plot(dw[0], Download1, Download2, Download3, Contouring)
