const timeDeff = (dateTimeStamp) => {
    let minute = 1000 * 60
    let hour = minute * 60
    let day = hour * 24
        // let halfamonth = day * 15
        // let month = day * 30

    let now = new Date().getTime()
    let diffValue = now - dateTimeStamp

    // let monthC = diffValue / month
    // let weekC = diffValue / (7 * day)
    let dayC = diffValue / day
    let hourC = diffValue / hour
    let minC = diffValue / minute
    let result = ''
    if (hourC >= 24) {
        result = parseInt(hourC / 24) + 'days ago'
    } else if (dayC > 1) {
        result = parseInt(dayC) + 'day ago'
    } else if (hourC >= 1) {
        result = parseInt(hourC) + 'hours ago'
    } else if (minC >= 1) {
        result = parseInt(minC) + 'minutes ago'
    } else {
        result = 'just now'
    }
    return result
}
export default timeDeff
