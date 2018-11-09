$(function () {
    $('#content .order').width(innerWidth)
    var orderid = $('.order h3').attr('orderid')
    $('.pay button').click(function () {
        console.log(111)
        $.get('/pay/',{'orderid':orderid},function (reponse) {
            console.log(reponse)
            window.open(reponse.Alipay,target='_self')
        })
    })
})