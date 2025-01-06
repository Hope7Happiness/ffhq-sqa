## Flickr-Faces-HQ Dataset (FFHQ)

__sqa 下载指南__

1. 首先，前往[链接](https://drive.google.com/drive/folders/1u2xu7bSrWxrbUxk-dT-UvEJq8IjdmNTP); 找到文件`ffhq-dataset-v2.json`，下载到`ffhq-sqa/`目录下.

2. 运行脚本下载数据集 (提前检查硬盘上至少需要90G的储存空间)

```bash
python download_ffhq.py --json --images
```

然后就会开始下载 (记得开梯子), 大约耗时2h. 
- NOTE: 中间有可能会断要定期检查，断了重新运行一遍会接着下载.

3. 结束！