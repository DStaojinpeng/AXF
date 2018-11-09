$(function () {
    $("#content .market").width(innerWidth);
    typeIndex = $.cookie('typeIndex');
    if (typeIndex) {
        $(".type-slider .type-item").eq(typeIndex).addClass("active")
    }
    else {
        $(".type-slider .type-item:first").addClass("active")
    }
    $(".type-item").click(function () {

        $.cookie("typeIndex", $(this).index(), {expires: 3, path: "/"});
    });
    // 分类
    $(".main-content").click(function () {
        sortViewHide();
        categoryViewHide();
    });
    // 全部类型 和排序
    categorybt = false;
    $("#categoryid").click(function () {
        categorybt = !categorybt;
        categorybt ? categoryViewShow() : categoryViewHide()
    });

    sortidbt = false;
    $("#sortid").click(function () {
        sortidbt = !sortidbt;
        sortidbt ? sortViewShow() : sortViewHide()
    });
    // 商品加
    // var num = $('.bt-wrapper .num').each().html()
    $('.bt-wrapper .num').each(function () {
        var num = parseInt($(this).html())
        if (num>0)
        {
            $(this).show()
            $(this).prev().show()
        }
        else
        {
            $(this).hide()
            $(this).prev().hide()
        }
    })

    $('.bt-wrapper .glyphicon-plus').click(function () {
        var $that = $(this)
        var goodsid = $that.attr("goodsid")
        $.get('/addcart/',{'goodsid':goodsid},function (response) {
            if (response.status == 1)
            {
                $that.prev().html(response.number)
                $that.prev().show().prev().show()
            }else
            {
                window.open(url='/login/',target="_self")
            }
        })
    })
    // 商品-
    $('.bt-wrapper .glyphicon-minus').click(function () {
        $that = $(this)
        var goodsid = $that.attr('goodsid')
        $.get('/subcart/',{'goodsid':goodsid},function (response) {
            console.log(response)
            if(response.status==1)
            {
                $that.next().html(response.number)
            }
            if (response.number==0)
            {
                 $that.hide()
                 $that.prev().hide()
            }
        })
    })
    function categoryViewShow() {
        sortidbt = false;
        sortViewHide();
        $(".bounce-view.category-view").show();
        $("#categoryid i").removeClass("glyphicon glyphicon-triangle-top").addClass('glyphicon glyphicon-triangle-bottom')

    }
    function categoryViewHide() {
        $(".bounce-view.category-view").hide();
        $("#categoryid i").removeClass("glyphicon glyphicon-triangle-bottom").addClass('glyphicon glyphicon-triangle-top')

    }
    function sortViewShow() {
        categorybt = false;
        categoryViewHide();
        $(".bounce-view.sort-view").show();
        $("#sortid i").removeClass("glyphicon glyphicon-triangle-top").addClass('glyphicon glyphicon-triangle-bottom')

    }
    function sortViewHide() {
        $(".bounce-view.sort-view").hide();
        $("#sortid i").removeClass("glyphicon glyphicon-triangle-bottom").addClass('glyphicon glyphicon-triangle-top')
    }


});