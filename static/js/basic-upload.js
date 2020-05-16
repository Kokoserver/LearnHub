var bt1 = document.getElementById("btn1") // on click on this button
 var coverPic = document = document.getElementById('id_cover_pic') // hidden input
 var text = document.getElementById('pic') // label
 btn1.addEventListener('click', ()=>{
   // input opener
   coverPic.click()})
 coverPic.addEventListener('change', function(){
   if(coverPic.value){
     if(coverPic.value.match(/\.(gif|jpe?g|tiff|png|webp|bmp)$/i)){
        text.innerHTML = coverPic.value}
     else if(coverPic.value.match(/\.(gif|jpe?g|tiff|png|webp|bmp)$/i) != true){
       text.innerHTML = 'Invalid cover image selected'
       text.style.color = 'red'}}
     else{
       text.innerHTML = 'No post cover pics selected yet'
       text.style.color = 'gray'}})

  var btn2 = document.getElementById("btn2") // pdf click button
  var pdf = document = document.getElementById('id_pdf') // hidden input
  var text2 = document.getElementById('pdf') // label

 // passing event to hidden input on click
  btn2.addEventListener('click', ()=>{
  pdf.click()})

// checking the hidden input file validity
    pdf.addEventListener('change', ()=>{
      if(pdf.value){
        if(pdf.value.match(/(pdf|msword)$|^text\/plain$/i)){
          text2.innerHTML = pdf.value
          text2.style.color = 'grey'}
        else if(!pdf.value.match(/(pdf|msword)$|^text\/plain$/i)){
          text2.innerHTML = 'Please select a valid file (pdf, text-file, msword etc)'
          text2.style.color = 'red'}}
      else{
          text2.innerHTML = 'No  document selected, yet'
          text2.style.color = 'gray'}})

    
function csrfSafeMethod(method) {
  //  these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$(document).ready(()=>{
  var button = document.getElementById('submit')

  //drag and drop
  // preventing page from redirecting
  $("html").on("dragover", (e)=>{
     e.preventDefault()
     e.stopPropagation()
  $("h1").text("Drag here")})

  $("html").on("drop", (e)=> { e.preventDefault(); e.stopPropagation()})

  $(()=> {
  // preventing page from redirecting
  $("html").on("dragover", (e)=> {
      e.preventDefault()
      e.stopPropagation()
      $("h1").text("Drag here")})

  $("html").on("drop", (e)=> {e.preventDefault(); e.stopPropagation()})

  // Handling files on Drag enter
  $('.upload-area').on('dragenter', (e)=> {
      e.stopPropagation();
      e.preventDefault();
      $("h1").text("Drop").css('color', 'gray')})

  var addThumbnail = (data)=>{
      $("#uploadfile h1").remove();
      let len = $("#uploadfile div.thumbnail").length;

  var num = Number(len),
      num = num + 1;
      name = data.name,
      size = convertSize(data.size),
      src = data.src

  // Creating an thumbnail
  $("#uploadfile").append('<div id="thumbnail_'+num+'" class="thumbnail"></div>');
  $("#thumbnail_"+num).append('<img src="'+src+'" width="100%" height="78%">');
  $("#thumbnail_"+num).append('<span class="size">'+size+'<span>')}

  // conerting the upload file size
  var convertSize=(size)=>{
  let sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB']
  if (size == 0) return '0 Byte';
  let i = parseInt(Math.floor(Math.log(size) / Math.log(1024)))
  return Math.round(size / Math.pow(1024, i), 2) + ' ' + sizes[i]}

  // handling file on Drag over
$('.upload-area').on('dragover',(e)=> {
      e.stopPropagation()
      e.preventDefault()
      $("h1").text("drop the file")})

   //  handling file on drop 
$('.upload-area').on('drop',(e)=> {
      e.stopPropagation()
      e.preventDefault()
      $("h1").text("Your file is added") //
      $("h1").css('margin-top', '2rem', 'color', 'gray')
      doc_file = e.originalEvent.dataTransfer.files})

  // Open file selector on div click
$("#uploadfile").click(()=>{
      $("#id_doc_file").click()})

   // handling  the doc file after a button is clicked
$("#id_doc_file").change(()=>{

    if($("#id_doc_file").val()){
       if($("#id_doc_file").val().match(/(\.|\/)(mp4)$/i)){$('h1').text('File is added')}
       else if(!$("#id_doc_file").val().match(/(\.|\/)(mp3|mp4)$/i)){
       $('h1').text('Please select a valid video file (mp4 format)').css('color', 'red')}}
    else{
    $('h1').text('No video pics selected, yet').css('color', 'gray')} })})

 $('#courseForm').submit(function(e){
   e.preventDefault();
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val(),
    duration = $("#id_duration").val(),  
    cover_pic = $('#id_cover_pic')[0].files,
    pdf = $('#id_pdf')[0].files,
    department = $("#id_department").val(),
    price = $("#id_amount").val(), 
    description =$("#id_description").val(),
    title = $("#id_title").val(),  
    file = $('#id_doc_file')[0].files,
    // getting and setting the message for error function
    errorOutput = (input, message)=>{ $(input).text(message).css('color', 'red')
    button.classList.add('disabled')}

    // checking if they are typing  to enable button disabled
    var onClickingOrChangeInInput=(input)=>{
      $(input).on('keypress change', ()=>{
      if(this){button.classList.remove('disabled')}})}
      // checking for each input
      onClickingOrChangeInInput($('#id_title'))
      onClickingOrChangeInInput($('#id_description'))
      onClickingOrChangeInInput($('#id_duration'))
      onClickingOrChangeInInput($('#id_department'))
      onClickingOrChangeInInput($('#id_price'))
    /// create alert list function
  var showError = (message)=>{
    if(button.classList.contains('disabled')){ $("#alert").modal('hide');}
    else{
      $("#alert").modal('show');
      $('.progress').hide()
      $('#errorMessage li').remove() // removing the previous error to prevent duplicate
      var error = document.createElement('li'),
      listStyle = {'color': 'red','padding-top': '5px','font-size':'16px' }
      error.appendChild(document.createTextNode(message))
      $('#alert ul').append(error).css(listStyle)
      $('.modal-title').text('Form error')
      $('#modal-btn2').hide()
      button.classList.add('disabled')}} // disable the  submit button if there error 
  

      if(!duration && !price && !department && !description &&  !title){
        // prevent showing if the submit button is disable
         if(button.classList.contains('disabled') == 1){
           $("#alert").modal('hide'); }
         else{
           showError(`
           Please fill in the form to continue,
           1. title
           2. description
           3. duration
           4. department
           5. price.
           Complete the form and
              __Upload all the files to complete the course upload.`)}}
     else{
      // checking if the inputs is empty
    if( title == ""){
        errorOutput('#title', 'Invalid title for this course')
        errorOutput('#description', 'Enter the title for this course')}
    else if( description == ""){
        errorOutput('#description', 'Invalid details given, please give details of the course')
        showError('Invalid description given, please give details of the course')}
    else if(duration == ""){
        showError('Enter the duration for this course')
        showError( "#duration", ' Specify the how many hours or minutes this course will take')}
    else if( department == ""){
        errorOutput('#department', "department can't be empty")
        showError('please enter the department that can take this course')}
    else if(  price == ""){
        errorOutput('#price', 'How much is the course e.g (2000)')
        showError(' Enter the price for this course')}
    else if($('#id_pdf').get(0).files.length === 0){
        errorOutput('#pic', 'Please select the cover picture')
        showError('Please select display picture for this course')}
    else if($('#id_doc_file').get(0).files.length === 0){
        errorOutput('#file', 'Please select the file to upload')
        showError('Please select files for this course')}
    else if(!pdf){
        errorOutput('#pdf', "Upload the attachment")
        showError('Please select the content to upload')}
    else if (duration && price && department && description && title && file && cover_pic){
      // validations checking if the inputs contains data 
      if(price.match(/^[0-9]+$/)){
        if(price < 500){
          errorOutput('#price', 'sorry price is not acceptable')}
        else if(price > 5000){
          errorOutput('#price', 'price exceed the expected')}}
      else{showError(`sorry price is expecting number but got ${price}`)}   
      if(typeof description === 'string'){
        if(department.length > 100){
          errorOutput('#department', 'department exceed the maximum character of 100')}
        else if(department.length < 5){
          errorOutput('#department', 'Minimum of 15 character is expected')}}
      else{showError('sorry only string is expected')}
      if(typeof description === 'string'){
        if(description.length < 50){errorOutput('#description', 'Minimum of 50 character is expected')}}
      else{showError('sorry only string is expected')}}
        // get the django csrf token from the form
      
      // initializing FormData 
      var form = new FormData()
      // assigning data input to FormData
      form.append('duration', $("#id_duration").val()),
      form.append('cover_pic', $('#id_cover_pic')[0].files),
      form.append('pdf', $('#id_pdf')[0].files),
      form.append('department', $("#id_department").val())
      form.append('amount', $("#id_amount").val())
      form.append('description',$("#id_description").val())
      form.append('title', $("#id_title").val())
      form.append('doc_file',  $('#id_doc_file')[0].files)
      form.append('csrftoken', $("[name=csrfmiddlewaretoken]").val())
      // this will print the formData values to the console
        //  for(var pair of form.entries()) {
        //   console.log(pair)}
  //  console.log()

      $.ajax({
        xhr: ()=> {
            var xhr = new window.XMLHttpRequest(),
            style ={' color':'white','background-color': 'green','align-text':'center'  }
            xhr.upload.addEventListener("progress", (evt)=> {
            if(file && cover_pic && department && duration && price && title && description){ // pdf attachment is optional
              if($('#id_cover_pic').get(0).files.length === 0 || $('#id_doc_file').get(0).files.length === 0){return}
              else if(evt.lengthComputable) {
                   var percentComplete = evt.loaded / evt.total,  progress
                   percentComplete = parseInt(percentComplete * 100);
                   $('#errorMessage ul li').remove() // removing the last error output in the modal
                   $("#alert").modal('show') // showing the modal
                   $('.modal-title').text('Uploading course') // updating the title
                   $('.progress').show() // showing the uploading progress in the modal
                   var progress = $('#progress').width(`${percentComplete}%`).text(`${percentComplete}%`) // updating the upload percent 
                  if (percentComplete === 100) {

                    // resetting the form after successful upload
                     $("#courseForm")[0].reset()
                     $('#pdf').text('please select attachments for material')
                     $('#pic').text('Upload the display image for your course')
                     $('.upload-area h1').text('Drag and Drop file here or Click to select file')
                      progress.css(style).text('completed')
                      // updating the title on 100% upload
                     $('.modal-title').text('Uploaded successfully')}}
            else{showError(`sorry can't upload the Course!,  try again`)}}}, false)
            return xhr},  
            type: "post",
            url: 'upload',
            data : new FormData(this),
            dataType: "json",
            contentType:false,
            processData:false,
            beforeSend: function(xhr, settings) {
              if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                  xhr.setRequestHeader("X-CSRFToken", csrftoken)}},
             success: (response)=>{console.log(response)}})
              }
         })
    
})

