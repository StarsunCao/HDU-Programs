const formatDate = (time) => {
    const date = new Date()
    date.setTime(time)

    const Days = ['日', '一', '二', '三', '四', '五', '六']
    let mounth = date.getMonth() + 1
    mounth = mounth < 10 ? 0 + mounth.toString() : mounth
    let day = date.getDay()
    let Day = date.getDate()
    Day = Day < 10 ? '0' + Day.toString() : Day
    const thisDay = Days[day]
    let minutes = date.getMinutes()
    minutes = minutes < 10 ? 0 + minutes.toString() : minutes
    let hours = date.getHours()
    hours = hours < 10 ? '0' + hours.toString() : hours
    let seconds = date.getSeconds()
    seconds = seconds < 10 ? '0' + seconds.toString() : hours
    const dataFormart = {
        fm1: '周' + thisDay,
        fm2: date.getFullYear() + '-' + mounth + '-' + Day + ' ' + hours + ':' + minutes + ':' + seconds + ' 周' + thisDay,
        fm3: date.getFullYear() + '-' + mounth + '-' + Day,
        fm4: date.getFullYear() + '-' + mounth + '-' + Day + ' 周' + thisDay,
        fm5: date.getFullYear() + '-' + mounth + '-' + Day + ' ' + hours + ':' + minutes + ':' + seconds
    }
    return (dataFormart)
}
export default formatDate