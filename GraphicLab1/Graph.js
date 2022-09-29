// i - номер вершины, n - количество вершин, t - положение кривой (от 0 до 1)
function getBezierBasis(i, n, t) {
	// Факториал
	function f(n) {
		return (n <= 1) ? 1 : n * f(n - 1);
	};
	
	// считаем i-й элемент полинома Берштейна
	return (f(n)/(f(i)*f(n - i)))* Math.pow(t, i)*Math.pow(1 - t, n - i);
}


// arr - массив опорных точек. Точка - двухэлементный массив, (x = arr[0], y = arr[1])
// step - шаг при расчете кривой (0 < step < 1), по умолчанию 0.01
function getBezierCurve(arr, step) {
	if (step == undefined) {
		step = 0.01;
	}
	
	var res = new Array()
	
	for (var t = 0; t < 1 + step; t += step) {
		if (t > 1) {
			t = 1;
		}
		
		var ind = res.length;
		
		res[ind] = new Array(0, 0);
		
		for (var i = 0; i < arr.length; i++) {
			var b = getBezierBasis(i, arr.length - 1, t);
			
			res[ind][0] += arr[i][0] * b;
			res[ind][1] += arr[i][1] * b;
		}
	}
	
	return res;
}


// ctx - rendering context холста, arr - массив точек по которым строим кривую
// delay - задержка перед отрисовкой следующей точки, pause - пауза перед началом  рисования,
function drawLines(ctx, arr, delay, pause) {
	if (delay == undefined) {
		delay = 10;
	}
	
	if (pause == undefined) {
		pause = delay;
	}
	var i = 0;
	
	function delayDraw() {
		if (i >= arr.length - 1) {
			return;
		}
		
		ctx.moveTo(arr[i][0],arr[i][1]);
		ctx.lineTo(arr[i+1][0],arr[i+1][1]);
		ctx.stroke();
	
		++i;
		
		setTimeout(delayDraw, delay);
	}
	
	setTimeout(delayDraw, pause);
}


drawC = document.getElementById('bezier');
drawC.width = document.width - 30;
drawC.height = document.height - 30;
		
if (drawC && drawC.getContext) {
	ctx = drawC.getContext('2d');
	ctx.fillStyle="#33CC99";
	ctx.lineWidth=0.1;
			
	var flow; // Массив координат кривой
	var arr = new Array();

	arr[0] = new Array(0, 100);
	arr[1] = new Array(100, 80);
	arr[2] = new Array(150, 150);
	arr[3] = new Array(200, 155);
	flow = getBezierCurve(new Array(arr[0], arr[1], arr[2], arr[3]), 0.01);
	drawLines(ctx, flow, 10);
}