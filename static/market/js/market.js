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