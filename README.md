# 2023年中国1 km土壤保持服务评估网格化数据集

**中文** | [English](README_EN.md)

2023年 · 中国 · 1 km × 1 km · GeoTIFF · t/(ha·a)

## 数据集简介

本数据集由首都师范大学胡卓玮教授课题组生产，是国家重点研发计划项目“大尺度生态质量与生态服务评估大数据智能挖掘技术和关键参数网格化平台建设应用示范”课题3（2023YFF1303703）形成的土壤保持服务评估数据产品。

数据集提供2023年中国全国尺度、1 km网格的年土壤保持量评估结果，**可以用于**全国及区域尺度土壤保持服务空间分布分析、生态系统服务综合评估，以及生态保护与修复相关研究；也可以结合研究区资料，为水土流失重点防治区识别、坡耕地治理布局、流域生态保护补偿及水土保持工程成效评估等研究提供基础数据。

## 基本信息

| 项目 | 内容 |
| --- | --- |
| 年份 | 2023年（单年度） |
| 空间范围 | 中国全国尺度；实际有效覆盖以栅格掩膜为准 |
| 空间分辨率 | 1000 m × 1000 m |
| 变量及单位 | 年土壤保持量（单位面积），t/(ha·a) |
| 数据格式 | GeoTIFF |
| 数据文件 | `China_Soil_Retention_Service_2023_1km.tif` |
| 文件大小 | 48,343,873字节，约46.10 MiB |
| 波段 / 数据类型 | 单波段 / Float32 |
| 栅格尺寸 | 4833列 × 5515行 |
| 坐标参考系统 | WGS 84基准的自定义Albers等积圆锥投影，坐标单位为米 |
| 投影参数 | 中央经线105°；原点纬度0°；标准纬线25°、47°；假东、假北均为0 m |
| XY坐标系 | Albers_Conic_Equal_Area |
| NoData | `-3.4028230607370965e+38` |
| 有效像元值域 | 0–34316.43359375 t/(ha·a) |
| 有效像元数 | 9,526,506 |
| 压缩方式 | LZW |
| 数据生产单位 | 首都师范大学 |
| 版本 | v1.0.0 |

空间参考、尺寸、NoData和值域来自原始GeoTIFF实读与全栅格检查；单位由数据提供者确认，原文件波段单位标签为空。完整元数据及投影坐标边界见[元数据文件](metadata/dataset_metadata.json)。WGS 84是基准，不表示本文件使用经纬度坐标（EPSG:4326）。

## 数据获取

请在本仓库的 [**Releases**](https://github.com/Hwx0513/ChinaSoilRetention-1km-2023/releases) 页面下载 `China_Soil_Retention_Service_2023_1km.tif` 和 `SHA256SUMS.txt`。数据文件保持原始内容，未进行重投影、重采样或数值修改。仓库的“Download ZIP”只包含说明、元数据和配图，不包含全国GeoTIFF。

下载后可使用 `sha256sum China_Soil_Retention_Service_2023_1km.tif`（Linux/macOS）或 `Get-FileHash China_Soil_Retention_Service_2023_1km.tif -Algorithm SHA256`（PowerShell）与校验文件核对。

## 技术方法

依据课题组填写的数据产品说明，本数据集基于修正通用土壤流失方程（RUSLE）开展年土壤保持量评估，对降雨侵蚀力因子进行以下优化：

1. 利用高时间分辨率GPM卫星降水数据识别侵蚀性降雨事件。
2. 引入RUSLE2降雨动能公式，增强对降雨侵蚀过程的表达。
3. 联合XGBoost与随机森林集成模型开展降雨侵蚀力空间降尺度。
4. 使用全国站点多年平均降雨侵蚀力基准数据开展偏差校正。

![数据生产技术流程（课题组提供）](figures/workflow.jpg)

## 质量评估及适用范围

以下为课题组数据产品说明中报告的内部评估结果，不代表已经通过现场核查或专家评审。本仓库未提供原始验证观测、模型生产代码及蒙特卡洛实验输入，以下指标未在本仓库中重新计算。

| 评估内容 | 报告结果 |
| --- | --- |
| 侵蚀输沙模拟验证 | 21个水文站，采用水文站输沙观测资料 |
| 所选站点平均RMSE | 250.48降至224.26 t/(km²·a)，下降10.47% |
| 蒙特卡洛模拟 | 优化后土壤保持量变异系数（CV）的空间汇总值为0.206 |
| 相对不确定性变化 | 在报告设定的输入与参数扰动条件下，较优化前降低46.19% |


## 空间分布示意

![2023年中国1 km土壤保持服务空间分布](figures/soil-retention-2023.png)

配图来自课题组提供的成果图，仅供浏览。定量分析请读取`China_Soil_Retention_Service_2023_1km.tif`，不要从配图颜色反推数值。

## 读取数据

可使用支持GeoTIFF的GIS软件打开文件，或安装Python的`rasterio`后运行：

```bash
python scripts/read_geotiff.py /path/to/China_Soil_Retention_Service_2023_1km.tif
```


## 相关研究论文

Zhao, L., Hu, Z., Wang, M., Liu, X., Hou, W., Wang, Y., Li, S., & Wang, J. (2025). Effects of Spatial Statistical Units on the Zoning of Ecosystem Soil Retention Services: A Case Study of the Loess Plateau. *Land Degradation & Development*. https://doi.org/10.1002/ldr.70171

## 数据使用声明

我们向科研群体提供数据产品，希望通过数据传播促进科学进步。如果您计划在论文或报告中使用本数据，请在研究早期告知我们，并确保您的研究与我们目前基于该数据产品开展的工作没有显著重叠。此外，如果本数据对您的研究至关重要，或某项重要结果或发现依赖于本数据，共同署名可能是适当的。请在论文投稿前充分提前告知您的分析和发表计划，给予我们阅读稿件并作出实质性学术贡献的机会，并在适当情况下邀请共同署名。联系人：Dr. Zhuowei Hu（huzhuowei@cnu.edu.cn）。


## 联系方式

| 联系人 | 邮箱 |
| --- | --- |
| 课题负责人：Dr. Zhuowei Hu（胡卓玮） | [huzhuowei@cnu.edu.cn](mailto:huzhuowei@cnu.edu.cn) |
| 技术联系人：Tianao Han | [2250902106@cnu.edu.cn](mailto:2250902106@cnu.edu.cn) |

## 下载统计

数据文件通过Release附件共享，附件下载次数可以通过[GitHub Releases API](https://docs.github.com/en/rest/releases/releases)中的`download_count`查看。统计时仅计入GeoTIFF附件，保留统计日期与版本；该次数不是独立用户数，也不等同于科研使用次数。具体操作见[数据下载说明](data/README.md)。
