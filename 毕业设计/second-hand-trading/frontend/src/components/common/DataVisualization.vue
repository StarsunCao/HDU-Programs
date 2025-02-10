<template>
    <div class="main-border">
        <div ref="lineChart" class="chart line-chart"></div>
        <div ref="pieChart" class="chart pie-chart"></div>
    </div>
</template>

<script>
    import * as echarts from 'echarts';
    export default {
        name: "DataVisualization",
        mounted() {
            this.initLineChart(); // 初始化折线图
            this.initPieChart(); // 初始化饼状图
        },
        methods:{
            initPieChart() {
                this.$api.countByLabel().then(res => {
                    const pieChartDom = this.$refs.pieChart;
                    const pieChart = echarts.init(pieChartDom);
                    const labels = ['数码科技', '生活用品', '运动相关', '图书笔记', '公告展示']; // 标签名称数组

                    // 构建饼状图的数据
                    const seriesData = labels.map((label, index) => ({
                        value: res[index], // 直接使用返回的数组中的值
                        name: label // 使用标签名称
                    }));

                    const pieOption = {
                        // 饼状图的配置
                        title: {
                            text: '商品类型分布',
                            subtext: '仅上架商品',
                            left: 'center'
                        },
                        tooltip: {
                            trigger: 'item',
                            formatter: '{a} <br/>{b} : {c} ({d}%)'
                        },
                        legend: {
                            orient: 'vertical',
                            left: 'left',
                            data: labels // 使用所有标签名称作为图例
                        },
                        series: [
                            {
                                name: '商品类型',
                                type: 'pie',
                                radius: '50%',
                                data: seriesData, // 使用构建的数据
                                emphasis: {
                                    itemStyle: {
                                        shadowBlur: 10,
                                        shadowOffsetX: 0,
                                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                                    }
                                }
                            }
                        ]
                    };
                    pieChart.setOption(pieOption);
                });
            },
            initLineChart() {
                // 定义一个数组来存储所有的操作类型
                const operationTypes = [0, 1, 2, 3, 4];
                const seriesPromises = operationTypes.map(type => {
                    // 为每种操作类型调用API
                    return this.$api.countByDay({ operationType: type });
                });

                // 等待所有的API调用完成
                Promise.all(seriesPromises).then(responses => {
                    console.log(responses);
                    // 确保responses数组中的每个元素都是有效的响应
                    if (responses.every(response => Array.isArray(response))) {
                        // 提取x轴的日期数据，假设所有操作类型的日期都相同
                        const dates = responses[0].map(item => item.operationDate);

                        // 提取每种操作类型的计数数据
                        const seriesData = responses.map((data, index) => ({
                            name: ['点击', '评论', '收藏', '下单', '上架'][index],
                            type: 'line',
                            data: data.map(item => item.count)
                        }));

                        var chartDom = this.$refs.lineChart;
                        var lineChart = echarts.init(chartDom);
                        var option;

                        option = {
                            title: {
                                text: '近7日数据统计图'
                            },
                            tooltip: {
                                trigger: 'axis'
                            },
                            legend: {
                                data: ['点击', '评论', '收藏', '下单', '上架']
                            },
                            grid: {
                                left: '3%',
                                right: '4%',
                                bottom: '3%',
                                containLabel: true
                            },
                            toolbox: {
                                feature: {
                                    saveAsImage: {}
                                }
                            },
                            xAxis: {
                                type: 'category',
                                data: dates // 使用从API获取的日期
                            },
                            yAxis: {
                                type: 'value'
                            },
                            series: seriesData
                        };

                        lineChart.setOption(option);
                }else {
                    console.error("API响应的数据格式不正确");
                }
            }).catch(error => {
                    console.error("获取数据失败:", error);
                });
            },

            handleCurrentChange(val) {
                this.nowPage = val;
                this.getOrder();
            },
            
        },
        data(){
            return {
                mode:1,
                nowPage: 1,
            }
        },
    }
</script>

<style scoped>
    .main-border{
        display: flex; /* 设置为Flex容器 */
        justify-content: center; /* 水平居中子元素 */
        align-items: center; /* 垂直居中子元素 */
        flex-wrap: wrap; /* 允许子元素在需要时换行 */
        background-color: #FFF;
        padding: 10px 30px;
        box-shadow: 0 1px 15px -6px rgba(0,0,0,.5);
        border-radius: 5px;
    }
    .chart {
        height: 500px; /* 设置高度 */
        margin: 10px; /* 为图表之间添加一些空间 */
    }
    .line-chart {
        flex: 2; /* 折线图占据更多空间 */
    }
    .pie-chart {
        flex: 1; /* 饼状图占据较少空间 */
    }
</style>