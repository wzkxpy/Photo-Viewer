
// 上传图片
let imgUpload = document.getElementById('imgUpload')
imgUpload.onchange = function (){
    const img_file = this.files[0]
    const form_data = new FormData()
    form_data.append('file', img_file)
    fetch('/post/add', {
        method: 'POST',
        body: form_data
    }).then()
}
// 设置顺序
let setOrder = document.getElementById('setOrder')
let showOrder = document.getElementById('showOrder')
const url = window.location.href;
if (url === 'http://127.0.0.1:5000/') {
    showOrder.innerText = '默认：正序'
    setOrder.setAttribute('href', '/id_asc')
}
else if (url === 'http://127.0.0.1:5000/id_asc') {
    showOrder.innerText = '默认：倒序'
    setOrder.setAttribute('href', '/time_desc')
}
else if (url === 'http://127.0.0.1:5000/time_desc') {
    showOrder.innerText = '时间：从晚到早'
    setOrder.setAttribute('href', '/time_asc')
}
else if (url === 'http://127.0.0.1:5000/time_asc') {
    showOrder.innerText = '时间：从早到晚'
    setOrder.setAttribute('href', '/address')
}
else if (url === 'http://127.0.0.1:5000/address') {
    showOrder.innerText = '地点'
    setOrder.setAttribute('href', '/')
}
