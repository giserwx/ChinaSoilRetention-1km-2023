# 数据下载 / Data download

本仓库的全国数据在 Releases 页面，文件为 `SC_2023.tif`（48,343,873字节）。请同时下载 `SHA256SUMS.txt` 核验完整性。仓库ZIP不含全国栅格。

The national raster is provided as `SC_2023.tif` in Releases. Download `SHA256SUMS.txt` to verify integrity. The repository ZIP does not include the raster.

## 下载次数 / Download counts

安装并登录GitHub CLI后，在仓库根目录运行以下命令，列出各版本GeoTIFF附件的下载次数：

With GitHub CLI installed and authenticated, run from the repository root:

```bash
gh api --paginate 'repos/{owner}/{repo}/releases' --jq '.[] | .tag_name as $tag | .assets[] | select(.name | endswith(".tif")) | [$tag, .name, .download_count] | @tsv'
```

保留统计日期、版本、文件名和次数；校验文件及其他附件不计入数据下载量。私有仓库的统计需要访问权限；正式公开时应记录初始次数，以便区分内部检查与后续下载。下载次数不能直接解释为独立使用者数或科研影响。

Record the retrieval date, version, asset name and count. Exclude checksums and other supporting assets. Private repositories require authenticated access. Record a baseline when making the repository public. Download counts do not directly measure unique users or research impact.

Source: [GitHub Releases API](https://docs.github.com/en/rest/releases/releases).
