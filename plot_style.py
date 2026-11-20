import matplotlib as mpl

C = {
    "blue"   : "#6B9AC4",
    "red"    : "#E08888",
    "green"  : "#7DB892",
    "purple" : "#A388BF",
    "orange" : "#E8A87C",
    "teal"   : "#7EBDC3",
    "sand"   : "#D4B896",
    "gray"   : "#8B8B8B",
}


def apply():
    mpl.rcParams.update({
        "font.family"        : "STIXGeneral",
        "font.serif"         : ["STIXGeneral", "DejaVu Serif"],
        "mathtext.fontset"   : "stix",
        "pdf.fonttype"       : 42,
        "ps.fonttype"        : 42,
        "font.size"          : 9,
        "axes.labelsize"     : 10,
        "axes.titlesize"     : 10,
        "xtick.labelsize"    : 8.5,
        "ytick.labelsize"    : 8.5,
        "legend.fontsize"    : 8.5,
        "figure.titlesize"   : 11,

        "figure.dpi"         : 150,
        "savefig.dpi"        : 300,
        "savefig.bbox"       : "tight",
        "savefig.pad_inches" : 0.05,
        "figure.facecolor"   : "white",

        "axes.spines.top"    : False,
        "axes.spines.right"  : False,
        "axes.linewidth"     : 0.7,
        "axes.labelpad"      : 3.5,
        "axes.titlepad"      : 6.0,
        "axes.prop_cycle"    : mpl.cycler("color", list(C.values())),

        "xtick.direction"    : "out",
        "ytick.direction"    : "out",
        "xtick.major.size"   : 3.0,
        "ytick.major.size"   : 3.0,
        "xtick.major.width"  : 0.7,
        "ytick.major.width"  : 0.7,
        "xtick.minor.size"   : 1.6,
        "ytick.minor.size"   : 1.6,

        "grid.color"         : "0.85",
        "grid.linewidth"     : 0.45,
        "grid.linestyle"     : "-",
        "axes.grid"          : False,

        "lines.linewidth"    : 1.4,
        "lines.markersize"   : 4.5,
        "lines.markeredgewidth": 0.8,

        "legend.frameon"     : True,
        "legend.framealpha"  : 0.92,
        "legend.edgecolor"   : "0.7",
        "legend.fancybox"    : False,
        "legend.borderpad"   : 0.35,
        "legend.handlelength": 1.8,
        "legend.handletextpad": 0.5,
        "legend.borderaxespad": 0.4,

        "text.usetex"        : False,
    })
