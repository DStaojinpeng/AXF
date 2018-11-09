$(function () {
    $('#content .cart').width(innerWidth)
    total()
    // 改变商品选取状态
    $(".confirm-wrapper").click(function () {
        $that = $(this)
        goodsid = $that.attr('goodsid')
        $.get('/change/', {'goodsid': goodsid}, function (response) {
            $that.find('span').remove()
            if (response.isselect === 'true') {
                $that.append('<span class="glyphicon glyphicon-ok" ></span>')
            }
            else {
                $that.append('<span class="no" ></span>')
            }
            // console.log(response.isselect)
            total()
        })

    })

//    全选
    $('.bill-left .all').click(function () {
        $that = $(this)
        isselect = $that.attr('isselect')
        isselect = (isselect == '1') ? 0 : 1
        $that.attr('isselect', isselect)
        if (isselect == 1) {
            $that.find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
        }
        else {
            $that.find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
        }
        $.get('/changeall/', {'isselect': isselect}, function (response) {
            if (response.status == '1') {
                $('.confirm-wrapper').each(function () {
                    $(this).attr('isselect', isselect)
                    if (isselect == 1) {
                        $(this).find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
                    }
                    else {
                        $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
                    }
                })
                total()
            }
        })

    })

    $('.bill-right').click(function () {

        if ($('.bill .total b').html() >0)
        {
            console.log($('.bill .total b').html())
            // var total=$('.bill .total b').html()
            $.get('/order/',{'total':total},function (response) {
                // console.log(response)
                if (response.status == 1)
                console.log(response)
                var orderid = response.orderid
                window.open('/orderdetail/'+response.orderid+'/',target='_self')
            })
        }
    })

    function total() {
        var sum = 0
        $('.cart ul li').each(function () {
            if ($(this).find('.confirm-wrapper').find('.glyphicon-ok').length) {
                var price = $(this).find('.price').attr('price')
                var num = $(this).find('.num').attr('num')
                sum += price * num
                console.log($('.confirm-wrapper').find('.glyphicon-ok').length)
            }
        })
        $('.bill .total b').html(sum)
        console.log(sum)
    }
})