import subprocess
from pathlib import Path
from matplotlib import font_manager, rcParams
import matplotlib.ticker as mtick
from matplotlib.ticker import MultipleLocator


# 定义一个函数,用于设置字体
def set_font(
    font_size=10,
    # 获取系统字体路径
    font_path=r"C:\Windows\Fonts\TimesSong.ttf"
):
    # 字体加载
    font_manager.fontManager.addfont(font_path)
    prop = font_manager.FontProperties(fname=font_path)
    # print(prop.get_name())  # 显示当前使用字体的名称

    # 字体设置
    rcParams["font.family"] = "sans-serif"  # 使用字体中的无衬线体
    rcParams["font.sans-serif"] = prop.get_name()  # 根据名称设置字体
    rcParams["font.size"] = font_size  # 设置字体大小
    rcParams["axes.unicode_minus"] = False  # 使坐标轴刻度标签正常显示正负号
    rcParams["svg.fonttype"] = "none"


def plot_as_emf(figure, **kwargs):
    # 获取inkscape_path
    inkscape_path = kwargs.get("inkscape_path", None)
    # 获取文件路径
    filepath = kwargs.get("filepath", None)
    # 获取dpi
    dpi = kwargs.get("dpi", 300)
    # 判断inkscape_path是否为空
    if inkscape_path is None:
        print("inkscape_path未指定")
    else:
        # 获取inkscape_path的路径
        inkscape_path = Path(inkscape_path).resolve()
    # 判断文件路径是否为空
    if filepath is not None:
        # 获取文件路径的路径
        filepath = Path(filepath).resolve()
        # 获取文件路径和文件名
        filepath, filename = filepath.parent, filepath.name
        filename = filepath.stem
        # 获取svg文件路径
        svg_filepath = filepath / f"{filename}.svg"
        # 获取emf文件路径
        emf_filepath = filepath / f"{filename}.emf"
        # 保存svg文件
        figure.savefig(svg_filepath, format="svg", dpi=dpi)
        # 将svg文件转换为emf文件
        subprocess.call(
            [inkscape_path, svg_filepath, "--export-type=emf", emf_filepath]
        )
        print(f"{emf_filepath} 生成成功")


# 定义一个函数,用于设置图表的样式
def set_style(
    ax,
    minorticks=True,
    x_minor=True,
    y_minor=True,
    xtick=None,
    yticks=None,
    visible_ticks_top_right=True,
    format=["%.1f", "%.1f"],
):

    '''设置图表的样式
    参数:
    ax:plt.axes对象,用于设置样式
    minorticks:bool,表示是否显示副刻度线
    x_minor:bool,表示是否显示x轴的副刻度线
    y_minor:bool,表示是否显示y轴的副刻度线
    xtick:float,表示x轴的主刻度线间隔
    yticks:float,表示y轴的主刻度线间隔
    visible_ticks_top_right:bool,表示是否去除上轴刻度
    format:list,表示x轴和y轴的主刻度线格式
    '''
    # 设置主刻度线间隔
    if xtick is not None:
        ax.xaxis.set_major_locator(MultipleLocator(xtick))
    if yticks is not None:
        ax.yaxis.set_major_locator(MultipleLocator(yticks))

    # 显示副刻度线
    if minorticks:
        ax.minorticks_on()

        # 获取 x 轴和 y 轴的主刻度线位置
        xticks = ax.get_xticks()
        yticks = ax.get_yticks()

        # 计算刻度线之间的差值
        xtick_interval = xticks[1] - xticks[0]
        ytick_interval = yticks[1] - yticks[0]

        # 设置副刻度线间隔
        if x_minor:
            ax.xaxis.set_minor_locator(MultipleLocator(xtick_interval * 0.5))
        else:
            ax.xaxis.set_minor_locator(MultipleLocator(xtick_interval))
        if y_minor:
            ax.yaxis.set_minor_locator(MultipleLocator(ytick_interval * 0.5))
        else:
            ax.yaxis.set_minor_locator(MultipleLocator(ytick_interval))
        # 修改有效小数位
        if format[0] is not None:
            ax.xaxis.set_major_formatter(mtick.FormatStrFormatter(format[0]))
        if format[1] is not None:
            ax.yaxis.set_major_formatter(mtick.FormatStrFormatter(format[1]))
    else:
        ax.minorticks_off()
    # 去除上轴刻度
    if not visible_ticks_top_right:
        # 去除上轴刻度
        visible_ticks = {
        "top": False,
        "right": False
        }
        ax.tick_params(axis="both", which="both",**visible_ticks)