async function copyContent(content) {
    // 复制结果
    let copyResult = true
    // 设置想要复制的文本内容
    const text = content || '代码复制失败';
    // 判断是否支持clipboard方式
    if (!!window.navigator.clipboard) {
        // 利用clipboard将文本写入剪贴板（这是一个异步promise）
        window.navigator.clipboard.writeText(text).then((res) => {
            Tips('复制成功');
            // 返回复制操作的最终结果
            return copyResult;
        }).catch((err) => {
            copyResult = false
            Tips('复制失败', err);
            // 返回复制操作的最终结果
            return copyResult;
        })
    } else {
        // 不支持clipboard方式 则采用document.execCommand()方式
        // 创建一个input元素
        let inputDom = document.createElement('textarea');
        // 设置为只读 防止移动端手机上弹出软键盘  
        inputDom.setAttribute('readonly', 'readonly');
        // 给input元素赋值
        inputDom.value = text;
        // 将创建的input添加到body
        document.body.appendChild(inputDom);
        // 选中input元素的内容
        inputDom.select();
        // 执行浏览器复制命令
        // 复制命令会将当前选中的内容复制到剪切板中（这里就是创建的input标签中的内容）
        // Input要在正常的编辑状态下原生复制方法才会生效
        const result = document.execCommand('copy')
        // 判断是否复制成功
        if (result) {
            Tips('复制成功');
        } else {
            Tips('复制失败');
            copyResult = false
        }
        // 复制操作后再将构造的标签 移除
        document.body.removeChild(inputDom);
        // 返回复制操作的最终结果
        return copyResult;
    }
}

async function Tips(content) {
    var tips_div = document.createElement('div');
    tips_div.id = 'Tips';
    tips_div.style.cssText = 'position: fixed;left: 50%;transform: translateX(-50%);top: 27px;min-width: 200px;height: 50px;border-radius: 25px;z-index: 9999;background: #51bce1cc;display: flex;justify-content: center;align-items: center;color: #ffffff;font-family: "Microsoft YaHei";text-align: center;';
    tips_div.innerHTML = content;
    tips_div.style.fontWeight = 'bold';
    tips_div.style.fontSize = 'medium';
    document.body.appendChild(tips_div);
    setTimeout(function () {
        document.body.removeChild(document.getElementById('Tips'));
    }, 2000);
}


async function loadFile(url) {
    try {
        const response = await fetch(url);
        const content = await response.text();
        return content;
    } catch (error) {
        console.error('无法读取文件:', error);
        return null;
    }
}


async function getFileToShow(elementId, filePath) {
    const getElementId = document.getElementById(elementId);
    const getFile = await loadFile(filePath);

    if (getFile !== null) {
        getElementId.textContent = getFile;


        // getElementId.dataset.highlighted = null; // 解除之前的高亮标记
        // hljs.highlightBlock(getElementId);
        hljs.highlightElement(getElementId);
        // hljs.highlight();
    }
}

// <script>中使用如下
/* (async function () {
    const getElementId = document.getElementById('fileContent');
    const getFile = await loadFile('openpyxlmd.py');

    if (getFile !== null) {
        getElementId.innerHTML = getFile;
        // getElementId.dataset.highlighted = null; // 解除之前的高亮标记
        // hljs.highlightBlock(getElementId);
        hljs.highlightElement(getElementId);
        hljs.highlight();
    }
})(); */