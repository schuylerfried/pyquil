def get_default_settings():
    """
    Return the default settings for the circuit drawing function to_latex().

    Returns:
        settings (dict): Default circuit settings
    """
    settings = dict()
    settings['gate_shadow'] = True
    settings['lines'] = ({'style': 'very thin', 'double_classical': True,
                          'init_quantum': True, 'double_lines_sep': .04})
    settings['gates'] = ({'HGate': {'width': .5, 'offset': .3,
                                    'pre_offset': .1},
                          'XGate': {'width': .35, 'height': .35,
                                    'offset': .1},
                          'SwapGate': {'width': .35, 'height': .35,
                                       'offset': .1},
                          'Rx': {'width': 1., 'height': .8, 'pre_offset': .2,
                                 'offset': .3},
                          'Ry': {'width': 1., 'height': .8, 'pre_offset': .2,
                                 'offset': .3},
                          'Rz': {'width': 1., 'height': .8, 'pre_offset': .2,
                                 'offset': .3},
                          'EntangleGate': {'width': 1.8, 'offset': .2,
                                           'pre_offset': .2},
                          'DeallocateQubitGate': {'height': .15, 'offset': .2,
                                                  'width': .2,
                                                  'pre_offset': .1},
                          'AllocateQubitGate': {'height': .15, 'width': .2,
                                                'offset': .1,
                                                'pre_offset': .1,
                                                'draw_id': False},
                          'MeasureGate': {'width': 0.75, 'offset': .2,
                                          'height': .5, 'pre_offset': .2}
                          })
    settings['control'] = {'size': .1, 'shadow': False}
    return settings


def _header(settings):
    """
    Writes the Latex header using the settings file.

    The header includes all packages and defines all tikz styles.

    Returns:
        header (string): Header of the Latex document.
    """
    packages = ("\\documentclass{standalone}\n\\usepackage[margin=1in]"
                "{geometry}\n\\usepackage[hang,small,bf]{caption}\n"
                "\\usepackage{tikz}\n"
                "\\usepackage{braket}\n\\usetikzlibrary{backgrounds,shadows."
                "blur,fit,decorations.pathreplacing,shapes}\n\n")

    init = ("\\begin{document}\n"
            "\\begin{tikzpicture}[scale=0.8, transform shape]\n\n")

    gate_style = ("\\tikzstyle{basicshadow}=[blur shadow={shadow blur steps=8,"
                  " shadow xshift=0.7pt, shadow yshift=-0.7pt, shadow scale="
                  "1.02}]")

    if not (settings['gate_shadow'] or settings['control']['shadow']):
        gate_style = ""

    gate_style += "\\tikzstyle{basic}=[draw,fill=white,"
    if settings['gate_shadow']:
        gate_style += "basicshadow"
    gate_style += "]\n"

    gate_style += ("\\tikzstyle{operator}=[basic,minimum size=1.5em]\n"
                   "\\tikzstyle{phase}=[fill=black,shape=circle," +
                   "minimum size={}".format(settings['control']['size']) +
                   "cm,inner sep=0pt,outer sep=0pt,draw=black"
                   )
    if settings['control']['shadow']:
        gate_style += ",basicshadow"
    gate_style += ("]\n\\tikzstyle{none}=[inner sep=0pt,outer sep=-.5pt,"
                   "minimum height=0.5cm+1pt]\n"
                   "\\tikzstyle{measure}=[operator,inner sep=0pt,minimum " +
                   "height={}cm, minimum width={}cm]\n".format(
                       settings['gates']['MeasureGate']['height'],
                       settings['gates']['MeasureGate']['width']) +
                   "\\tikzstyle{xstyle}=[circle,basic,minimum height=")
    x_gate_radius = min(settings['gates']['XGate']['height'],
                        settings['gates']['XGate']['width'])
    gate_style += ("{x_rad}cm,minimum width={x_rad}cm,inner sep=0pt,"
                   "{linestyle}]\n"
                   ).format(x_rad=x_gate_radius,
                            linestyle=settings['lines']['style'])
    if settings['gate_shadow']:
        gate_style += ("\\tikzset{\nshadowed/.style={preaction={transform "
                       "canvas={shift={(0.5pt,-0.5pt)}}, draw=gray, opacity="
                       "0.4}},\n}\n")
    gate_style += "\\tikzstyle{swapstyle}=["
    gate_style += "inner sep=-1pt, outer sep=-1pt, minimum width=0pt]\n"
    edge_style = ("\\tikzstyle{edgestyle}=[" + settings['lines']['style'] +
                  "]\n")

    return packages + init + gate_style + edge_style


def _footer():
    """
    Return the footer of the Latex document.

    Returns:
        tex_footer_str (string): Latex document footer.
    """
    return "\n\n\end{tikzpicture}\n\end{document}"

