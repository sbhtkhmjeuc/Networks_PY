# TO DO: import modules
import socket

# TO DO: set constants
IP = '127.0.0.1'
PORT = 8020
SOCKET_TIMEOUT = 0.1


def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client """
    # TO DO : add code that given a resource (URL and parameters) generates the proper response
    data = "HTTP/1.1 200 OK\r\n"
    data += "Content-Type: text/html; charset=utf-8\r\n"
    data += "\r\n"
    data += ''' 
    
    <html>
<head>
	<meta charset="UTF-8">
	<title>Gvahim Test Site</title>
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
	<link rel="shortcut icon" href="imgs/favicon.ico"> 
	<link rel="stylesheet" type="text/css" href="css/doremon.css">
	<style>
	body {
		overflow: hidden;
		font-family: Arial, Helvetica, sans-serif;
		font-weight: 300;
	}
	a {
		text-decoration: none;
	}
	.st-container {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		left: 0;
		font-family: 'Josefin Slab', 'Myriad Pro', Arial, sans-serif;
	}

	.st-container > input,
	.st-container > a {
		position: fixed;
		bottom: 0px;
		width: 20%;
		cursor: pointer;
		font-size: 16px;
		height: 34px;
		line-height: 34px;
	}

	.st-container > input {
		opacity: 0;
		z-index: 1000;
	}

	.st-container > a {
		z-index: 10;
		font-weight: 700;
		background: #79BD9A; /*e23a6e*/
		background: #79BD9A;
		color: #fff;
		text-align: center;
		text-shadow: 1px 1px 1px rgba(151,24,64,0.2);
	}

	/* "Fix" for percentage rounding: add a background bar pseudo element with the same color like the labels */
	.st-container:before {
		content: '';
		position: fixed;
		width: 100%;
		height: 34px;
		background: #79BD9A; /*e23a6e*/
		background: #79BD9A;
		z-index: 9;
		bottom: 0;
	}

	#st-control-1, #st-control-1 + a {
		left: 0;
	}

	#st-control-2, #st-control-2 + a {
		left: 20%;
	}

	#st-control-3, #st-control-3 + a {
		left: 40%;
	}

	#st-control-4, #st-control-4 + a {
		left: 60%;
	}

	#st-control-5, #st-control-5 + a {
		left: 80%;
	}

	.st-container > input:checked + a,
	.st-container > input:checked:hover + a{
		background: #3B8686; /*821134*/
		background: #3B8686;
	}

	.st-container > input:checked + a:after,
	.st-container > input:checked:hover + a:after{
		bottom: 100%;
		border: solid transparent;
		content: '';
		height: 0;
		width: 0;
		position: absolute;
		pointer-events: none;
		border-bottom-color: #3B8686; /*821134*/
		border-width: 20px;
		left: 50%;
		margin-left: -20px;
	}

	.st-container > input:hover + a{
		background: #3B8686; /*AD244F*/
	}

	.st-container > input:hover + a:after {
		border-bottom-color: #3B8686; /*AD244F*/
	}

	.st-scroll,
	.st-panel {
		position: relative;
		width: 100%;
		height: 100%;
	}

	.st-scroll {
		top: 0;
		left: 0;
		-webkit-transition: all 0.6s ease-in-out;
		-moz-transition: all 0.6s ease-in-out;
		-o-transition: all 0.6s ease-in-out;
		-ms-transition: all 0.6s ease-in-out;
		transition: all 0.6s ease-in-out;

		/* Let's enforce some hardware acceleration */
		-webkit-transform: translate3d(0, 0, 0);
		-webkit-backface-visibility: hidden;
	}

	.st-panel{
		background: #fff;
		overflow-y: scroll;
		overflow-x: hidden;
	} 

	#st-control-1:checked ~ .st-scroll {
		-webkit-transform: translateY(0%);
		-moz-transform: translateY(0%);
		-o-transform: translateY(0%);
		-ms-transform: translateY(0%);
		transform: translateY(0%);
	}
	#st-control-2:checked ~ .st-scroll {
		-webkit-transform: translateY(-100%);
		-moz-transform: translateY(-100%);
		-o-transform: translateY(-100%);
		-ms-transform: translateY(-100%);
		transform: translateY(-100%);
	}
	#st-control-3:checked ~ .st-scroll {
		-webkit-transform: translateY(-200%);
		-moz-transform: translateY(-200%);
		-o-transform: translateY(-200%);
		-ms-transform: translateY(-200%);
		transform: translateY(-200%);
	}
	#st-control-4:checked ~ .st-scroll {
		-webkit-transform: translateY(-300%);
		-moz-transform: translateY(-300%);
		-o-transform: translateY(-300%);
		-ms-transform: translateY(-300%);
		transform: translateY(-300%);
	}
	#st-control-5:checked ~ .st-scroll {
		-webkit-transform: translateY(-400%);
		-moz-transform: translateY(-400%);
		-o-transform: translateY(-400%);
		-ms-transform: translateY(-400%);
		transform: translateY(-400%);
	}


	/* Content elements */

	.st-deco{
		width: 200px;
		height: 200px;
		position: absolute;
		top: 0px;
		left: 50%;
		margin-left: -100px;
		background: #A8DBA8; /*fa96b5*/
		-webkit-transform: translateY(-50%) rotate(45deg);
		-moz-transform: translateY(-50%) rotate(45deg);
		-o-transform: translateY(-50%) rotate(45deg);
		-ms-transform: translateY(-50%) rotate(45deg);
		transform: translateY(-50%) rotate(45deg);
	}

	[data-icon]:after {
		content: attr(data-icon);
		font-family: 'FontAwesome';
		color: #fff;
		text-shadow: 1px 1px 1px rgba(151,24,64,0.2);
		position: absolute;
		width: 200px;
		height: 200px;
		line-height: 200px;
		text-align: center;
		font-size: 90px;
		top: 50%;
		left: 50%;
		margin: -100px 0 0 -100px;
		-webkit-transform: rotate(-45deg) translateY(25%);
		-moz-transform: rotate(-45deg) translateY(25%);
		-o-transform: rotate(-45deg) translateY(25%);
		-ms-transform: rotate(-45deg) translateY(25%);
		transform: rotate(-45deg) translateY(25%);
	}

	.st-panel h2 {
		color: #79BD9A; /*e23a6e*/
		text-shadow: 1px 1px 1px rgba(151,24,64,0.2);
		position: absolute;
		font-size: 54px;
		font-weight: 900;
		width: 80%;
		left: 10%;
		text-align: center;
		line-height: 50px;
		margin: -70px 0 0 0;
		padding: 0;
		top: 25%;
		-webkit-backface-visibility: hidden;
	}

	#st-control-1:checked ~ .st-scroll #st-panel-1 h2,
	#st-control-2:checked ~ .st-scroll #st-panel-2 h2,
	#st-control-3:checked ~ .st-scroll #st-panel-3 h2,
	#st-control-4:checked ~ .st-scroll #st-panel-4 h2,
	#st-control-5:checked ~ .st-scroll #st-panel-5 h2{
		-webkit-animation: moveDown 0.6s ease-in-out 0.2s backwards;
		-moz-animation: moveDown 0.6s ease-in-out 0.2s backwards;
		-o-animation: moveDown 0.6s ease-in-out 0.2s backwards;
		-ms-animation: moveDown 0.6s ease-in-out 0.2s backwards;
		animation: moveDown 0.6s ease-in-out 0.2s backwards;
	}
	@-webkit-keyframes moveDown{
		0% { 
			-webkit-transform: translateY(-40px); 
			opacity: 0;
		}
		100% { 
			-webkit-transform: translateY(0px);  
			opacity: 1;
		}
	}

	@-moz-keyframes moveDown{
		0% { 
			-moz-transform: translateY(-40px); 
			opacity: 0;
		}
		100% { 
			-moz-transform: translateY(0px);  
			opacity: 1;
		}
	}

	@-o-keyframes moveDown{
		0% { 
			-o-transform: translateY(-40px); 
			opacity: 0;
		}
		100% { 
			-o-transform: translateY(0px);  
			opacity: 1;
		}
	}

	@-ms-keyframes moveDown{
		0% { 
			-ms-transform: translateY(-40px); 
			opacity: 0;
		}
		100% { 
			-ms-transform: translateY(0px);  
			opacity: 1;
		}
	}

	@keyframes moveDown{
		0% { 
			transform: translateY(-40px); 
			opacity: 0;
		}
		100% { 
			transform: translateY(0px);  
			opacity: 1;
		}
	}

	.st-panel p, .st-centered {
		position: absolute;
		text-align: center;
		font-size: 16px;
		/*line-height: 22px;*/
		color: #8b8b8b;
		z-index: 2;
		padding: 0;
		width: 100%;
		left: 0%;
		top: 25%;
		margin: 10px 0 0 0;
		-webkit-backface-visibility: hidden;
	}
	#st-control-1:checked ~ .st-scroll #st-panel-1 p, .st-centered,
	#st-control-2:checked ~ .st-scroll #st-panel-2 p, .st-centered,
	#st-control-3:checked ~ .st-scroll #st-panel-3 p, .st-centered,
	#st-control-4:checked ~ .st-scroll #st-panel-4 p, .st-centered,
	#st-control-5:checked ~ .st-scroll #st-panel-5 p, .st-centered{
		-webkit-animation: moveUp 0.6s ease-in-out 0.2s backwards;
		-moz-animation: moveUp 0.6s ease-in-out 0.2s backwards;
		-o-animation: moveUp 0.6s ease-in-out 0.2s backwards;
		-ms-animation: moveUp 0.6s ease-in-out 0.2s backwards;
		animation: moveUp 0.6s ease-in-out 0.2s backwards;
	}

	@-webkit-keyframes moveUp{
		0% { 
			-webkit-transform: translateY(40px); 
			opacity: 0;
		}
		100% { 
			-webkit-transform: translateY(0px);  
			opacity: 1;
		}
	}

	@-moz-keyframes moveUp{
		0% { 
			-moz-transform: translateY(40px); 
			opacity: 0;
		}
		100% { 
			-moz-transform: translateY(0px);  
			opacity: 1;
		}
	}

	@-o-keyframes moveUp{
		0% { 
			-o-transform: translateY(40px); 
			opacity: 0;
		}
		100% { 
			-o-transform: translateY(0px);  
			opacity: 1;
		}
	}

	@-ms-keyframes moveUp{
		0% { 
			-ms-transform: translateY(40px); 
			opacity: 0;
		}
		100% { 
			-ms-transform: translateY(0px);  
			opacity: 1;
		}
	}

	@keyframes moveUp{
		0% { 
			transform: translateY(40px); 
			opacity: 0;
		}
		100% { 
			transform: translateY(0px);  
			opacity: 1;
		}
	}

	/* Colored sections */

	.st-color,
	.st-deco{
		background: #A8DBA8; /*fa96b5*/
	}
	.st-color [data-icon]:after {
		color: #A8DBA8; /*fa96b5*/
	}
	.st-color .st-deco {
		background: #fff;
	}
	.st-color h2 {
		color: #fff;
		text-shadow: 1px 1px 1px rgba(0,0,0,0.1);
	} 
	.st-color p, .st-color .st-centered {
		color: #fff;
		color: rgba(255,255,255,0.8);
	}

	@media screen and (max-width: 520px) {
		.st-panel h2 {
			font-size: 38px;
			top: 35%;
			margin-bottom: 15px;
		}

		.st-box {
			margin: 10px auto 60px 0px !important;
			display:block !important;
		}

		.st-panel p, .st-centered{
			top: 30% !important;
			width: 90%;
			left: 5%;
			margin-top: 10px;
			margin-bottom: 50px;
		}

		.st-container > a {
			font-size: 13px;
		}
	}
	@media screen and (max-width: 399px) {
		.st-panel h2 {
			font-size: 27px;
			top: 30%;
			margin-bottom: 15px;
		}

		.st-box {
			margin: 10px auto 60px 0px !important;
			display:block !important;
		}

		.st-panel p, .st-centered{
			top: 30% !important;
			width: 90%;
			left: 5%;
			margin-top: 10px;
			margin-bottom: 50px;
		}

		.st-container > a {
			font-size: 10px;
		}

		.st-deco{
			width: 120px;
			height: 120px;
			margin-left: -60px;
		}

		[data-icon]:after {
			font-size: 60px;
			-webkit-transform: rotate(-45deg) translateY(15%);
			-moz-transform: rotate(-45deg) translateY(15%);
			-o-transform: rotate(-45deg) translateY(15%);
			-ms-transform: rotate(-45deg) translateY(15%);
			transform: rotate(-45deg) translateY(15%);
		}
	}
	</style>
	<style>

	.st-box {
		/*width: 300px;
		height: 200px;
		box-shadow: inset 1px 1px 40px 0 rgba(0, 0, 0, .45);
		border-bottom: 2px solid #fff;
		border-right: 2px solid #fff;
		margin: 5% auto 0 auto;
		*/
		/*background: url(http://ianfarb.com/wp-content/uploads/2013/10/nicholas-hodag.jpg);*/
		background-size: cover;
		border-radius: 5px;
		overflow: hidden;
		display:inline-block;
		margin: 10px 20px 40px auto;
	}
	.box-holder {
		height: 300px;
	}

	.st-box #overlay {
		background: rgba(0, 0, 0, .75);
		text-align: center;
		padding: 45px 0 66px 0;
		opacity: 0;
		-webkit-transition: opacity .25s ease;
		-moz-transition: opacity .25s ease;
	}

	.st-box:hover #overlay {
		opacity: 1;
	}

	.st-box #plus {
		font-family: Helvetica;
		font-weight: 900;
		color: rgba(255, 255, 255, .85);
		font-size: 96px;
	}
	.info {
		margin-top: 8px;
		width: 300px;
		height: 100px;
		margin: auto;
	}
	#box{
		background:gray;
		width:50px; height:50px;
		position: relative;
		top:0px; left:0px;
		border-radius:10px;
		font-size: 10px;
		text-align: center;
		color: #fff;
		cursor: pointer;
	}
	#box:hover{
		background:#fa96b5;


	}
	</style>
	<style>
	* {
		box-sizing: border-box;
	}

	.row {

		font-family: "Open Sans", sans-serif;
		font-weight: 300;
		color: #fff;
		max-width: 800px;
		margin: 0 auto;
		padding: 20px 30px 60px;
		position: relative;
		z-index: 1;
		text-align: center;
	}
	.row:before {
		position: absolute;
		content: "";
		display: block;
		top: 0;
		left: -5000px;
		height: 100%;
		width: 15000px;
		z-index: -1;
	}

	.row span {
		position: relative;
		display: inline-block;
		margin: 30px 10px;
	}


	.row span:last-of-type {
		margin: 5px 10px 20px 10px;
	}

	.row span:first-of-type {
		margin: 10px 10px 30px;
	}


	.swing {
		display: inline-block;
		width: 280px;
		padding: 11px 0 10px 15px;
		font-family: Arial, Helvetica, sans-serif;
		font-weight: 400;
		color: #377D6A;

		background: #efefef;
		border: 0;
		border-radius: 3px;
		outline: 0;
		text-indent: 125px;
		transition: all .3s ease-in-out;
	}
	.swing::-webkit-input-placeholder {
		color: #efefef;
		text-indent: 0;
		font-weight: 300;
	}
	.swing + label {
		display: inline-block;
		position: absolute;
		top: 0;
		left: 0;
		padding: 9px 15px;
		text-shadow: 0 1px 0 rgba(19, 74, 70, 0.4);
		background: #377D6A ;
		border-top-left-radius: 3px;
		border-bottom-left-radius: 3px;
		transform-origin: 2px 2px;
		transform: rotate(0);
		-webkit-animation: swing-back .4s 1 ease-in-out;
		-moz-animation: swing-back .4s 1 ease-in-out;
		-o-animation: swing-back .4s 1 ease-in-out;
		animation: swing-back .4s 1 ease-in-out;
	}

	@-webkit-keyframes swing {
		0% {
			transform: rotate(0);
		}
		20% {
			transform: rotate(116deg);
		}
		40% {
			transform: rotate(60deg);
		}
		60% {
			transform: rotate(98deg);
		}
		80% {
			transform: rotate(76deg);
		}
		100% {
			transform: rotate(82deg);
		}
	}
	@-moz-keyframes swing {
		0% {
			transform: rotate(0);
		}
		20% {
			transform: rotate(116deg);
		}
		40% {
			transform: rotate(60deg);
		}
		60% {
			transform: rotate(98deg);
		}
		80% {
			transform: rotate(76deg);
		}
		100% {
			transform: rotate(82deg);
		}
	}
	@-o-keyframes swing {
		0% {
			transform: rotate(0);
		}
		20% {
			transform: rotate(116deg);
		}
		40% {
			transform: rotate(60deg);
		}
		60% {
			transform: rotate(98deg);
		}
		80% {
			transform: rotate(76deg);
		}
		100% {
			transform: rotate(82deg);
		}
	}
	@keyframes swing {
		0% {
			transform: rotate(0);
		}
		20% {
			transform: rotate(116deg);
		}
		40% {
			transform: rotate(60deg);
		}
		60% {
			transform: rotate(98deg);
		}
		80% {
			transform: rotate(76deg);
		}
		100% {
			transform: rotate(82deg);
		}
	}

	@-webkit-keyframes swing-back {
		0% {
			transform: rotate(82deg);
		}
		100% {
			transform: rotate(0);
		}
	}
	@-moz-keyframes swing-back {
		0% {
			transform: rotate(82deg);
		}
		100% {
			transform: rotate(0);
		}
	}
	@-o-keyframes swing-back {
		0% {
			transform: rotate(82deg);
		}
		100% {
			transform: rotate(0);
		}
	}
	@keyframes swing-back {
		0% {
			transform: rotate(82deg);
		}
		100% {
			transform: rotate(0);
		}
	}

	.swing:focus,
	.swing:active {
		color: #377D6A;
		text-indent: 0;
		background: #fff;
		border-top-left-radius: 0;
		border-bottom-left-radius: 0;
	}
	.swing:focus::-webkit-input-placeholder,
	.swing:active::-webkit-input-placeholder {
		color: #aaa;
	}
	.swing:focus + label,
	.swing:active + label {
		-webkit-animation: swing 1.4s 1 ease-in-out;
		-moz-animation: swing 1.4s 1 ease-in-out;
		-o-animation: swing 1.4s 1 ease-in-out;
		animation: swing 1.4s 1 ease-in-out;
		transform: rotate(82deg);
	}


	
	.balloon {
		display: inline-block;
		width: 215px;
		padding: 10px 0 10px 15px;
		font-family: "Open Sans", sans;
		font-weight: 400;
		color: #377D6A;
		background: #efefef;
		border: 0;
		border-radius: 3px;
		outline: 0;
		text-indent: 60px;
		transition: all .3s ease-in-out;
	}
	.balloon::-webkit-input-placeholder {
		color: #efefef;
		text-indent: 0;
		font-weight: 300;
	}
	.balloon + label {
		display: inline-block;
		position: absolute;
		top: 8px;
		left: 0;
		bottom: 8px;
		padding: 5px 15px;
		color: #032429;
		font-size: 11px;
		font-weight: 700;
		text-transform: uppercase;
		text-shadow: 0 1px 0 rgba(19, 74, 70, 0);
		transition: all .3s ease-in-out;
		border-radius: 3px;
		background: rgba(122, 184, 147, 0);
	}
	.balloon + label:after {
		position: absolute;
		content: "";
		width: 0;
		height: 0;
		top: 100%;
		left: 50%;
		margin-left: -3px;
		border-left: 3px solid transparent;
		border-right: 3px solid transparent;
		border-top: 3px solid rgba(122, 184, 147, 0);
		transition: all .3s ease-in-out;
	}

	.balloon:focus,
	.balloon:active {
		color: #377D6A;
		text-indent: 0;
		background: #fff;
	}
	.balloon:focus::-webkit-input-placeholder,
	.balloon:active::-webkit-input-placeholder {
		color: #aaa;
	}
	.balloon:focus + label,
	.balloon:active + label {
		color: #fff;
		text-shadow: 0 1px 0 rgba(19, 74, 70, 0.4);
		background: #7ab893;
		transform: translateY(-40px);
	}
	.balloon:focus + label:after,
	.balloon:active + label:after {
		border-top: 4px solid #7ab893;
	}


	</style>
	<style>
	.results {
		margin: 30px;
		
		color: #0B486B;
		color: #FE4365;
		
		font-weight: 900;
	}
	.button-submit {
		background: #fff;
		-webkit-box-shadow: 0 0 0 2px #4cd964;
		box-shadow: 0 0 0 2px #4cd964;
		border: 0;
		height: 40px;
		line-height: 36px;
		width: 120px;
		font-weight: 900;
		font-size: 14px;
		color: #4cd964;
		position: absolute;
		/* top: 50%; */
		left: 50%;
		top:84%;
		-webkit-transform: translate(-50%, -50%);
		-moz-transform: translate(-50%, -50%);
		-o-transform: translate(-50%, -50%);
		-ms-transform: translate(-50%, -50%);
		transform: translate(-50%, -50%);
		-webkit-border-radius: 20px;
		border-radius: 20px;
		-webkit-transition: all 0.2s ease;
		-moz-transition: all 0.2s ease;
		-o-transition: all 0.2s ease;
		-ms-transition: all 0.2s ease;
		transition: all 0.2s ease;
		cursor: pointer;
		outline: none;
	}
	.button-submit:hover {
		background: #4cd964;
		color: #fff;
	}
	.button-submit.pro {
		background-color: #b5b5b5;
		background-image: url("imgs/loading.gif");
		background-repeat: no-repeat;
		background-position: center center;
		-webkit-box-shadow: 0 0 0 2px #b5b5b5;
		box-shadow: 0 0 0 2px #b5b5b5;
		color: #fff;
		-webkit-transition: background-color 0.2s ease;
		-moz-transition: background-color 0.2s ease;
		-o-transition: background-color 0.2s ease;
		-ms-transition: background-color 0.2s ease;
		transition: background-color 0.2s ease;
	}
	.button-submit.finish {
		background: #4cd964;
		-webkit-box-shadow: 0 0 0 2px #4cd964;
		box-shadow: 0 0 0 2px #4cd964;
		-webkit-transition: background-color, border-color 0.2s ease;
		-moz-transition: background-color, border-color 0.2s ease;
		-o-transition: background-color, border-color 0.2s ease;
		-ms-transition: background-color, border-color 0.2s ease;
		transition: background-color, border-color 0.2s ease;
	}
	.button-submit.finish:after {
		content: "";
		display: block;
		position: absolute;
		width: 14px;
		height: 6px;
		border-bottom: 4px #fff solid;
		border-left: 4px #fff solid;
		z-index: 9999;
		-webkit-transform: rotate(-45deg);
		-moz-transform: rotate(-45deg);
		-o-transform: rotate(-45deg);
		-ms-transform: rotate(-45deg);
		transform: rotate(-45deg);
		margin: -7px 0px 0px 44px;
		-webkit-animation: fade 0.8s ease forwards;
		-moz-animation: fade 0.8s ease forwards;
		-o-animation: fade 0.8s ease forwards;
		-ms-animation: fade 0.8s ease forwards;
		animation: fade 0.8s ease forwards;
	}
	#reset {
		position: absolute;
		top: 75%;
		left: 50%;
		-webkit-transform: translate(-50%, -50%);
		-moz-transform: translate(-50%, -50%);
		-o-transform: translate(-50%, -50%);
		-ms-transform: translate(-50%, -50%);
		transform: translate(-50%, -50%);
		color: #b5b5b5;
		cursor: pointer;
		font-size: 12px;
	}
	@-moz-keyframes fade {
		0% {
			opacity: 0;
			-ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
			filter: alpha(opacity=0);
		}
		100% {
			opacity: 1;
			-ms-filter: none;
			filter: none;
		}
	}
	@-webkit-keyframes fade {
		0% {
			opacity: 0;
			-ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
			filter: alpha(opacity=0);
		}
		100% {
			opacity: 1;
			-ms-filter: none;
			filter: none;
		}
	}
	@-o-keyframes fade {
		0% {
			opacity: 0;
			-ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
			filter: alpha(opacity=0);
		}
		100% {
			opacity: 1;
			-ms-filter: none;
			filter: none;
		}
	}
	@keyframes fade {
		0% {
			opacity: 0;
			-ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
			filter: alpha(opacity=0);
		}
		100% {
			opacity: 1;
			-ms-filter: none;
			filter: none;
		}
	}

	</style>



</head>

<body>

	<div class="container">

		<div class="st-container">
			
			<input type="radio" name="radio-set" checked="checked" id="st-control-1"/>
			<a href="#st-panel-1">4.4 File Types</a>

			<input type="radio" name="radio-set" id="st-control-2"/>
			<a href="#st-panel-2">4.5/6 Functions calculate-next</a>

			<input type="radio" name="radio-set" id="st-control-3"/>
			<a href="#st-panel-3">4.9 Functions calculate-area</a>

			<input type="radio" name="radio-set" id="st-control-4"/>
			<a href="#st-panel-4">4.10 Post</a>

			<input type="radio" name="radio-set" id="st-control-5"/>
			<a href="#st-panel-5">4.11 Get Posted Image</a>

			<div class="st-scroll">
				
				<!-- Placeholder text from http://hipsteripsum.me/ -->

				<section class="st-panel" id="st-panel-1">
					<div class="st-deco" data-icon="✦"></div>
					<h2>4.4 File Types</h2>
					<div class="st-centered">
						<div class="st-box">
							<div class="doraemon">
								<div class="face">
									<div class="base-white"></div>
									<div class="lefteye eye eye-left">
										<div class="leftblackeye black-eye black-left"></div>
									</div>
									<div class="righteye eye eye-right">
										<div class="rightblackeye black-eye black-right"></div>
									</div>
									<div class="nose">
										<div class="nose-line"></div>
									</div>
									<div class="mouth"></div>
									<div class="whiskers whi-right whi-top"></div>
									<div class="whiskers whi-right whi-mid"></div>
									<div class="whiskers whi-right whi-bottom"></div>
									<div class="whiskers whi-left whi-top"></div>
									<div class="whiskers whi-left whi-mid"></div>
									<div class="whiskers whi-left whi-bottom"></div>
								</div>
							</div>
							<!--<div class="info">Support Css File Type And Then try mouseover Doraemon!</div> -->
							<div class="info">Support CSS File Type </br>CSS Is A Language Used By Web Developers To Style <u>Now move the mouse over Doraemon!</u> (Find The Css For Doreamon)</div>
						</div>
						<div class="st-box">
							<div class="">
								<img src="imgs/abstract.jpg" class="face" />
							</div>
							<!-- <div class="info">Support jpg File Type try to support png, bmp, gif as well</div> -->
							<div class="info">Support JPG File Type </br>Images Are All Over The Web Support Them Most Common Formats Are JPG, BMP, PNG Gif (Animated)</div>
						</div>
						<div class="st-box">
							<div class="box-holder">
								<div id="box"></div>
							</div>
							
							<!--<div class="info">Support js File Type And Then try to click the box!</div>-->
							<div class="info">Support JS File Type </br>JavaScript Is A Language Used By Web Developers To Create Interactions <u>Now Click On The Box! Click Again and Again</u> (Find The js For The Box)</div>
						</div>
					</div>
				</section>

				<section class="st-panel st-color" id="st-panel-2">
					<div class="st-deco" data-icon="✦"></div>
					<h2>4.5/6 Functions calculate-next</h2>
					<div class="st-centered">
						<div class="st-box">
							<div class="row">
								<div id="CalculateNextResult" class="results">Click Submit To See Result:</div>
								<span>
									<input class="swing" id="CalculateNext" type="text" placeholder="Int Number" /><label for="CalculateNext">Calculate Next</label>
								</span>
								<button id="CalculateNextSubmit" class="button-submit">Submit</button>
							</div>
							<div class="info">Support The Calc Next Function Then Press The Button</div>
						</div>
					</div>
				</section>

				<section class="st-panel" id="st-panel-3">
					<div class="st-deco" data-icon="✦"></div>
					<h2>4.9 Functions calculate-area</h2>
					<div class="st-centered">
						<div class="st-box">
							<div class="row">
								<div id="CalculateAreaResult" class="results">Click Submit To See Result:</div>
								<span>
									<input class="balloon" id="CalculateAreaHeight" type="text" placeholder="Int Area Height" /><label for="CalculateAreaX">Height</label>
								</span>
								<span>
									<input class="balloon" id="CalculateAreaWidth" type="text" placeholder="Int Area Width" /><label for="CalculateAreaX">Width</label>
								</span>
								<button id="CalculateAreaSubmit" class="button-submit">Submit</button>
								
							</div>
							<div class="info">Support The Calc Area Function Then Press The Button</div>
						</div>
					</div>
				</section>

				<section class="st-panel st-color" id="st-panel-4">
					<div class="st-deco" data-icon="✦"></div>
					<h2>4.10 Post</h2>
					<div class="st-centered">
						<div class="st-box">
							<div class="row">
								<div id="PostImageResult" class="results">Click Submit To See Result:</div>
								<span>
									<input class="balloon" id="PostImage" type="file" placeholder="Choose..." /><label for="PostImage">File</label>
								</span>
								<button id="PostImageSubmit" class="button-submit">Submit</button>
								
							</div>
							<div class="info">Support The POST Image Function Then Press The Button</div>
						</div>
					</div>
				</section>

				<section class="st-panel" id="st-panel-5">
					<div class="st-deco" data-icon="✦"></div>
					<h2>4.11 Get Posted Image</h2>
					<div class="st-centered">
						<div class="st-box">
							<div class="row">
								<div id="GetImageResult" class="results">Click Submit To See Result:</div>
								<span>
									<input class="balloon" id="GetImage" type="text" placeholder="String Image Name" /><label for="GetImage">Image</label>
								</span>
								<button id="GetImageSubmit" class="button-submit">Submit</button>
								
							</div>
							<div class="info">Support The Get Image Function Then Press The Button</div>
						</div>
					</div>
				</section>

			</div><!-- // st-scroll -->

		</div><!-- // st-container -->

	</div>
	<script type="text/javascript" src="js/jquery.min.js"></script>
	<script type="text/javascript" src="js/box.js"></script>
	
	<script type="text/javascript" src="js/submit.js"></script>

</body>
</html>

    
    '''
    client_socket.send(data.encode())
    return None

def validate_http_request(request):

    valid_http = True
    request_array = request.decode().rsplit()
    print(request_array)
    if request_array[0] != "GET":
        valid_http = False
    if request_array[2] != "HTTP/1.1":
        valid_http = False

    resource = request_array[1]
    resource = resource.replace('/', '\\')
    return valid_http, resource

def handle_client(client_socket):
    print('Client connected')

    while True:
        client_request = client_socket.recv(2048)
        valid_http, resource = validate_http_request(client_request)
        if valid_http:
            print('Got a valid HTTP request')
            handle_client_request(resource, client_socket)
            break
        else:
            print('Error: Not a valid HTTP request')
            break

    print('Closing connection')
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print("Listening for connections on port {}".format(PORT))

    while True:
        client_socket, client_address = server_socket.accept()
        print('New connection received')
        client_socket.settimeout(SOCKET_TIMEOUT)
        handle_client(client_socket)


if __name__ == "__main__":
    # Call the main handler function
    main()