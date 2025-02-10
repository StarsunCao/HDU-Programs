var left = echarts.init(document.getElementById("l"),"dark");
var loption = {
  legend: {
    top: 'bottom'
  },
  toolbox: {
    show: true,
    feature: {
      mark: { show: true },
      dataView: { show: true, readOnly: false },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  series: [
    {
      name: 'Nightingale Chart',
      type: 'pie',
      radius: [20, 150],
      center: ['50%', '50%'],
      roseType: 'area',
      itemStyle: {
        borderRadius: 8
      },
      data: [
        { value: 0, name: '商品 1' },
        { value: 0, name: '商品 2' },
        { value: 0, name: '商品 3' },
        { value: 0, name: '商品 4' },
        { value: 0, name: '商品 5' },
        { value: 0, name: '商品 6' },
        { value: 0, name: '商品 7' },
        { value: 0, name: '商品 8' }
      ]
    }
  ]
};
left.setOption(loption);