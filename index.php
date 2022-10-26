<!DOCTYPE html>
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

        <script src="js/prism_logic.js"></script>
        <!-- see here for more info -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.23.0/prism.min.js"></script>
        <link rel='stylesheet' href='css/prism.css' type='text/css'>
        
        <!-- PRODUCTION / Brightspace: if we need to put it back in brightspace - it needs the CSS local
        <script src="https://learn.inside.dtu.dk/content/enforced/137173-OFFERING-Sandbox-41WPG/prism_logic.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.23.0/prism.min.js"></script>
        <script>
            document.head.innerHTML += "<link rel='stylesheet' href='https://learn.inside.dtu.dk/content/enforced/137173-OFFERING-Sandbox-41WPG/prism.css' type='text/css'/>";
        </script>
        -->

    </head>
    <body>
        <div style="width:100%">
            <h1 style="float:left;margin-left:10px;margin-bottom:0px;margin-top:-10px;"> IfcHtmlHack</h1> 
            <div style="float:right;">
                
                <label style="float:left" for="project">project:</label>
                <select name="project" id="project">
                    <option value="1337">1337</option>
                    <option value="duplex">duplex</option>
                    <option value="duplex2">duplex2</option>
                    <option value="duplex3">duplex3</option>
                    <option value="01">01</option>
                    <option value="05">05</option>
                    <option value="06">06</option>
                    <option value="09">09</option>
                    <option value="11">11</option>
                </select><br>
            </div>
        </div><br>
        <!-- this is the prism code that allows us to display and edit the code-->
        <!-- TODO: Think how to alternatively show the result - iframe? i know... but what are the other options?-->

        <!-- some buttons with hardcoded links to the files ... -->
        <!-- TODO: Turn this into a function ? are we allowed PHP? -->
        <div style="width:100%;float:left">
            
            <button style="float:right" onclick="window.open(getFileName('html'));">View Page</button>
            <? //php $div = $div->getElementById('editing');?>
            <div style="float:none">
            <form method="post" id="usrform">
                <textarea name="textdata" form="usrform"cols="80" rows="80" placeholder="Enter HTML Source Code" id="editing" spellcheck="false" oninput="update(this.value); sync_scroll(this);" onscroll="sync_scroll(this);" onkeydown="check_tab(this, event);"></textarea>
                <pre id="highlighting" aria-hidden="true"><code class="language-css" id="highlighting-content"></code></pre>
                <input style="float:right"type="submit" name="submit" VALUE ="Save">
                <input style="float:right" type="text" name="url" id="url">
            </form>
        </div>
            <button style="float:left" onclick="popIt(getFileName('html')); document.getElementById('highlighting-content').className ='language-html';">Load HTML</button>
            <button style="float:left" onclick="popIt(getFileName('css'));document.getElementById('highlighting-content').className ='language-css';">Load CSS</button>
            <button style="float:left" onclick="popIt(getFileName('js'));document.getElementById('highlighting-content').className ='language-js';">Load JS</button>
        </div>

        <?php
          
            if(isset($_POST['textdata']))
            {
                $data=$_POST['textdata'];
                $string = $_POST['url'];
                $fp = fopen($string, 'w');
                fwrite($fp, $data);
                fclose($fp);
            }
        ?>
        
        <script type="text/javascript">

            /* This is all taken from teh original prism example
            TODO: Clean it up ...*/

        function getFileName(file)
        {
            var file_name= 'nothing';
            var project = $("#project").val(); // The value of the selected option
            if (file=='html') {
                file_name = project+'/index.html';
            }
            else if (file=='css'){
                file_name = project+'/css/main.css';
            }
            else if (file=='js'){
                file_name = project+'/js/main.js';
            }
            document.getElementById('url').value = file_name;
            return(file_name);

        }    
        
        function saveTextAsFile()
        {
            var textToSave = document.getElementById("editing").value;
            var textToSaveAsBlob = new Blob([textToSave], {type:"text/plain"});
            var textToSaveAsURL = window.URL.createObjectURL(textToSaveAsBlob);
            var fileNameToSaveAs = document.getElementById("inputFileNameToSaveAs").value;
        
            var downloadLink = document.createElement("a");
            downloadLink.download = fileNameToSaveAs;
            downloadLink.innerHTML = "Download File";
            downloadLink.href = textToSaveAsURL;
            downloadLink.onclick = destroyClickedElement;
            downloadLink.style.display = "none";
            document.body.appendChild(downloadLink);
        
            downloadLink.click();
        }
        function destroyClickedElement(event)
        {
            document.body.removeChild(event.target);
        }
        function popIt(file_name)
        {
            // PRODUCTION: if we need to put it back in brightspace - it is currently junking out all the html....
            // var file = "https://learn.inside.dtu.dk/content/enforced/137173-OFFERING-Sandbox-41WPG/"+name;

            // TODO: This should be edited so that it just gets the selected group 
            var file = file_name;

            $.get( file, function( data ) {
                document.getElementById("editing").value = data;
                console.log(document.getElementById("editing").value);
                update(document.getElementById("editing").value);
            });
        
        }
        
        function loadFileAsText()
        {
            var fileToLoad = document.getElementById("fileToLoad").files[0];
        
            var fileReader = new FileReader();
            fileReader.onload = function(fileLoadedEvent) 
            {
                var textFromFileLoaded = fileLoadedEvent.target.result;
                document.getElementById("inputTextToSave").value = textFromFileLoaded;
            };
            fileReader.readAsText(fileToLoad, "UTF-8");
        }
        
        </script>
    
    </body>

</html>