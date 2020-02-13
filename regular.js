

$(()=>{

    // let result = $('div') //searching for all div elements
    // console.log(result)
    // $('#paragraph') //to get ID 
    // let $result = $(".myImage")
    // always add $ even to your variables so you know what is JS and what is JQuery
    $('div').html("<span style= 'background-color: yellow; font-size:30px'>This is a great day</span>") 
    //^^ This is adding html within the tags. So basically adding tags within the div.

    //creating elements
    // let $a = $('<a>');
    // //you can create attributes too
    let $a = $('<a>', {
        'class': 'myAnchor',
        'text': 'digital Crafts',
        'href': "https://digitalcrafts.com/"

    });
    $('div').append($a); 

    let $img = $('<img>', {
        'src': 'https://cdn2-www.dogtime.com/assets/uploads/gallery/30-impossibly-cute-puppies/impossibly-cute-puppy-2.jpg',
        'alt': 'image of puppies'
    })
    $('div').append($img)

    // $('p').removeClass('myImage');

    // $('p').click(()=>{
    //     alert('you clicked on the yellow box')

    // })
    // $('p').on('click', ()=>{
    //     alert('you clicked on the yellow box')

    // })

    // $('body').keydown((e)=>{
    //     //e just means any key
    //     console.log(`Key Down: ${e.keyCode}`);
    // })

    // $('body').keyup((e)=>{
    //     console.log(`Key Up: ${e.keyCode}`);
    // })
    let $inputCount = $('input')
    $('input').keyup((e)=>{
        console.log($inputCount.val().length);
        $('#count').html($inputCount.val().length);
    })
})

//$ sign represents JQuery