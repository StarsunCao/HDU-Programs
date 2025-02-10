//柱状图
var right = echarts.init(document.getElementById("r"),"dark");

var roption;

roption = {

  title: {
    text: '商品特征图',
    subtext: '价格/销售额'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: ['价格', '销售额']
  },
  toolbox: {
    show: true,
    feature: {
      dataView: { show: true, readOnly: false },
      magicType: { show: true, type: ['line', 'bar'] },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  calculable: true,
  xAxis: [
    {
      type: 'category',
      // prettier-ignore
      data: ['商品1', '商品2', '商品3', '商品4', '商品5']
    }
  ],
  yAxis: [
    {
      type: 'value'
    }
  ],
  series: [
    {
      name: '价格',
      type: 'bar',
      data: [0, 0, 0, 0, 0],
      markPoint: {
        data: [
          { type: 'max', name: 'Max' },
          { type: 'min', name: 'Min' }
        ]
      },
      markLine: {
        data: [{ type: 'average', name: 'Avg' }]
      }
    },
    {
      name: '销售额',
      type: 'bar',
      data: [0, 0, 0, 0, 0],
      markPoint: {
        data: [
          { name: 'Max', value: 182.2, xAxis: 7, yAxis: 183 },
          { name: 'Min', value: 2.3, xAxis: 11, yAxis: 3 }
        ]
      },
      markLine: {
        data: [{ type: 'average', name: 'Avg' }]
      }
    }
  ]
};
right.setOption(roption);