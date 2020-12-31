
var CenterX = 0;
var CenterY = 0;
for (var i = 0; i < CarsNum; i++)
{
    CenterX += CarsPos[i]['carPosX'];
    CenterY += CarsPos[i]['carPosY'];
}
var center = [CenterX/CarsNum, CenterY/CarsNum]; // 中心点

        // var position = new AMap.LngLat(116, 39);//标准写法 经度在前 纬度在后
        // var position = [116.397428, 39.90923]; // 简写
        var map = new AMap.Map('container', {
            resizeEnable: true, //是否监控地图容器尺寸变化
            zoom: 11, //初始化地图层级
            center: center, //初始化地图中心点
        });
        // map.setMapStyle('amap://styles/darkblue');

        var markers = []; // 标记点
        for (var i = 0; i < CarsNum; i++)
        {
            position = [CarsPos[i]['carPosX'], CarsPos[i]['carPosY']];
            icon_str = "";
            if (CarsPos[i]['carIsUse'] == 'True') icon_str = "https://webapi.amap.com/theme/v1.3/markers/n/mark_r.png";
            markers[i] = new AMap.Marker({
                position: position,
                title: '序号：' + CarsPos[i]['carid']+' 车牌：'+ CarsPos[i]['carLicense'] + ' 电量：' + CarsPos[i]['carEQ'],
                icon: icon_str,
            })
        }

        // var marker1 = new AMap.Marker({
        //     position: [116.39, 39.9], //位置
        //     title: '市中心',
        // });

        // var marker2 = new AMap.Marker({
        //     position: [116.45, 39.9], //位置
        //     title: '标记2',
        //      icon: "https://webapi.amap.com/theme/v1.3/markers/n/mark_r.png",
        // }) # todo 添加红色图标在这

        // map.add(marker1);//添加到地图
        // map.add(marker2);//添加到地图

        map.add(markers);

        AMap.plugin([
            'AMap.ToolBar',
            'AMap.Scale',
            'AMap.OverView',
            'AMap.MapType',
            'AMap.Geolocation',
        ], function () {
            // 在图面添加工具条控件，工具条控件集成了缩放、平移、定位等功能按钮在内的组合控件
            map.addControl(new AMap.ToolBar());

            // 在图面添加比例尺控件，展示地图在当前层级和纬度下的比例尺
            map.addControl(new AMap.Scale());

            // 在图面添加鹰眼控件，在地图右下角显示地图的缩略图
            // map.addControl(new AMap.OverView({isOpen: true}));

            // 在图面添加类别切换控件，实现默认图层与卫星图、实施交通图层之间切换的控制
            map.addControl(new AMap.MapType());

            // 在图面添加定位控件，用来获取和展示用户主机所在的经纬度位置
            map.addControl(new AMap.Geolocation());
        });


         // 地图事件的点击
        var clickHandler = function (e) {
            alert('您在[ ' + e.lnglat.getLng() + ',' + e.lnglat.getLat() + ' ]的位置点击了地图!' + CarsNum);
        };

        // 绑定事件
        map.on('click', clickHandler);
        // 解绑事件
        // map.off('click', clickHandler);
        MoreBtn = document.getElementsByClassName("btn btn-danger btn-sm"); // 详情按钮
    // todo 1、这里整体的视图适应已经完成，下面要修改的是将车按照可约、在使用、损坏进行分类标记为绿色、红色、灰色
    // todo 2、然后是对面板的每一个详情进行点击时，地图缩放到该对应车的面板。
    for (var i = 0; i < MoreBtn.length;i++) { // 对每个元素实施点击事件
        MoreBtn[i].onclick = function () {
            map.setFitView(markers);
        };
    }
        // document.querySelectorAll("#MoreBtn").onclick=function () {
        //     map.setFitView();
        // }

       // Dom控制详情事件
       //  var MoreBtn = document.querySelectorAll("#MoreBtn");
        // var listener = AMap.event.addDomListener(MoreBtn, "click", function(ev) {
        //     // DOM 被点击时触发，ev 为原生事件
        //     alert("点击了详情"); // 在这里修改事件
        //     });
        // 解绑事件
        // AMap.event.removeListener(listener);