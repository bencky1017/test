# NPM镜像

可以直接修改镜像

## 默认镜像

```sh
npm config set registry https://registry.npmjs.org/
```

## 镜像站

```sh
npm config set registry https://registry.npmmirror.com/
```

## 淘宝镜像

```sh
npm config set registry https://registry.npm.taobao.org/
```



## 临时参数形式

在执行命令时候添加参数，比如安装socket.io时候使用`镜像站`的`registry`：

```sh
npm install socket.io --registry=https://registry.npmmirror.com
```

