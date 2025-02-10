
var map = echarts.init(document.getElementById("c"),"dark");
var mydata = [{
	'name':'上海','value':162},
	{'name': '广东', 'value': 316},
	{'name': '江苏', 'value': 40},
	{'name': '广东', 'value': 19},
	{'name': '北京', 'value': 16},
	{'name': '广东', 'value': 14},
	{'name': '湖南', 'value': 14},
	{'name': '江苏', 'value': 10},
	{'name': '上海', 'value': 10},
	{'name': '浙江', 'value': 8},
	{'name': '广东', 'value': 7},
	{'name': '浙江', 'value': 7},
	{'name': '四川', 'value': 6},
	{'name': '河南', 'value': 3},
	{'name': '山东', 'value': 2},
	{'name': '吉林', 'value': 2}
]
var optionMap = {
		title: {
			text: '',
			subtext: '',
			x: 'left'
		},
		tooltip: {
			trigger: 'item'
		},
		//左侧小导航图标
		visualMap: {
			show: true,
			x: 'left',
			y: 'bottom',
			textStyle: {
				fontSize: 8
			},
			splitList: [{
					start: 1,
					end: 9
				},
				{
					start: 10,
					end: 99
				},
				{
					start: 100,
					end: 999
				},
				{
					start: 1000,
					end: 9999
				},
				{
					start: 10000
				}
			],
			color: ['#8A3310','#C64918', '#E55B25','#F2AD92', '#F9DCD1']
		},

			//配置属性
			series: [{
				name: '发货商数量',
				type: 'map',
				mapType: 'china',
				roam: false,
				itemStyle: {
					normal: {
						borderWidth: .5,
						borderColor: '#009fe8',
						areaColor: '#ffefd5'
					},
					emphasis: {
						borderWidth: .5,
						borderColor: '#4b0082',
						areaColor: '#fff'
					}
				},
				label: {
					normal: {
						show: true, //省份名称
						fontSize: 8
					},
					emphasis: {
						show: true,
						fontSize: 8
					}
				},
				data: mydata //数据
			}]
		};

		//使用制定的配置项和数据显示图表
		map.setOption(optionMap);
