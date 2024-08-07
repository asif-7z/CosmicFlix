console.log("js loaded");

// var bi = document.querySelector("bki")
// bi.classList.add("bki")

// var a = document.getElementById("devil")
// var b  = a.innerHTML
// var ele  = document.getElementById("asf")

//  var ti = document.getElementById("title").classList.add("titl")


// var getstyle = document.getElementById("asf")
// console.log(window.getComputedStyle(getstyle).fontSize)

// interval = setInterval(function(){
//   b = b>0 ?  b -= 1 : 0
//     a.innerHTML = b

//  size =  ele.style.fontSize = 10*b+"px"
//  console.log(size)
//  if (b<=0){
//   clearInterval(interval)
//  }
// },1000)


// var input = document.getElementById("non");
// var bd = document.querySelector("body")



// input.addEventListener("click",function(){
//   // alert("rgb("+Math.floor(Math.random()*255)+","+Math.floor(Math.random()*255)+","+Math.floor(Math.random()*255)+")")
//   bd.style.backgroundColor = "rgb("+Math.floor(Math.random()*255)+","+Math.floor(Math.random()*255)+","+Math.floor(Math.random()*255)+")"
// } )


// var em = document.getElementById("usernameid")
// em.addEventListener("focus",function(){
//   console.log("true")
// })

// em.addEventListener("blur",function(){
//   console.log("blured")
// })

// document.body.addEventListener('keydown',function(e){
//   var keyCode = e.keyCode;
//   if (keyCode === 13){

  
//     console.log(keyCode+"key is down")
//     }     
// })

// document.body.addEventListener('keyup',function(e){
//   var keyCode = e.keyCode;
//   if (keyCode === 13){

  
// console.log(keyCode+"key is up")
// }
// })
// document.body.addEventListener('keypress',function(e){
//   var keyCode = e.keyCode;
//   if (keyCode === 13){

  
// console.log(keyCode+"key is pressed")
// }
// })
// var btn = document.getElementById("non")
// btn.addEventListener("mousedown",function(){
//   console.log("mouse is down ")
// })

// btn.addEventListener("mouseup",function(){
//   console.log("mouse is up ")
// })
// btn.addEventListener("click",function(){
//   console.log("mouse is clicked ")
// })
// btn.addEventListener("dblclick",function(){
//   console.log("mouse is doubleclicked ")
// })
// btn.addEventListener("mouseover",function(){
//   console.log("mouse is over ")
// })
// btn.addEventListener("mouseenter",function(){
//   console.log("mouse is entered")
// })
// btn.addEventListener("mousemove",function(){
//   console.log("mouse is moved ")
// })

// var btn = document.getElementById('non')
// var bd = document.getElementById("fn")
// var first = document.getElementById("title")
// var listitem = document.getElementById("listitem")
// value = '';
// listitem.addEventListener('input',function(e){
//     value = e.target.value
// })
// // var num =0;
// btn.addEventListener('click',function(){
//   if (listitem.value !== null && listitem.value !== '' && listitem.value !== undefined){

  
//   var newelement = document.createElement('li')
//   var addtxt = document.createTextNode(value)
//   var ele = newelement.appendChild(addtxt)
//   bd.appendChild(newelement)
//   // bd.insertBefore(newelement,first)
  
//   listitem.value = ''
//   value  = ''
//   }
//   else {
//     alert("please enter the item")
//   }


// })

// var btn = document.getElementById('non')
// var first = document.getElementById('fn')

// btn.addEventListener('click',function(){
//      firstitem = first.firstElementChild;
//      first.removeChild(firstitem)

//      //first.replaceChild()




// });

// var input = document.getElementById('listitem')
// var error = document.getElementById("usernameerror")
// input.addEventListener('input',function(e){
//     var str = e.target.value;
//     var pattern = /^[\w]{8}[\d]{4}$/g
//     var check = pattern.test(str)
//     if (check){
//      error.style.display = "none";
//     }
//     else{
//         error.style.display = "block";

//     }

// })


// function createNewElement(title){
//     var newelement = document.createElement('li')
//     var addtxt = document.createTextNode(title)
//     newelement.appendChild(addtxt)
    
    
//     return newelement
    
//     }

// var bd = document.getElementById("fn")
// function jsonGet(){
//     var http = new XMLHttpRequest;
//     http.onreadystatechange = function(){
//         if(this.readyState === 4)
//         {
//             if(this.status === 200)
//             {
//                 responsedata = JSON.parse(this.responseText)
//                 for(var i = 0;i<responsedata.length;i++)
//                 {
//                     lists = createNewElement(responsedata[i].title)
//                     bd.append(lists)

//                 }
//             }
//             else{
//                 console.log("ressponse not completed")
//             }
//         }
//     }
//     http.open('GET','https://jsonplaceholder.typicode.com/todos',true)
//     http.send()
// }


// jsonGet()



// var input = document.getElementById('listitem')
// var value = '';
// input.addEventListener('input',function(e){
//     value = e.target.value;
// })

// function createNewElement(title){
//             var newelement = document.createElement('li')
//             var addtxt = document.createTextNode(title)
//             newelement.appendChild(addtxt)
            
            
//             return newelement
            
// }

// var bd = $("#fn")

// var btn = $('#non')

// btn.click(function jsonPost(){
//     var http = new XMLHttpRequest;
//     http.open('POST','https://jsonplaceholder.typicode.com/todos',true)
//     obj = JSON.stringify({
//         "userId": 1,
//         "title": value,
//         "compleated": false
//     })
//     http.send(obj)
//     http.onreadystatechange = function(){
//         if(this.readyState === 4){
//             if(this.status === 201)
//             {
//                 var newele = JSON.parse(this.responseText)
//                 console.log(newele)
//                 bd.append(createNewElement(value))
//             }
//             else
//             {
//                 console.log("not completed")
//             }
            
//         }
//     }
// }
// )
$('#titl').addClass('newc');
$('.bck').addClass('bki');
console.log("hello")

var srn = $('#vh')
var tit = $('#pl');



// srn.mouseover(function(){
//      $('#pl').addClass('tnt')

// })

// srn.mouseleave(function(){
//     $('#pl').removeClass('tnt')
// })

