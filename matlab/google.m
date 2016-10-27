http1Time = [341649931, 335621287, 335870495, 317391290, 330918724, 339473841, 342426606, 345767708, 1224867579, 1158170265, 1176418466, 328873338, 336229688, 336816657, 344462688, 329407184, 337554561, 334389989, 336654091, 329864807, 341145377, 336339298, 339965864, 340497361, 1242285266, 340027179, 1222691636, 329742273, 340207242, 332521416, 332026851, 334451505, 330124595, 275605770, 340005486, 282778628, 334952868, 338567407, 344964754, 347800100, 338954410, 302578765, 343372689, 316162069, 338778829, 331439352, 335958536, 1228641960, 336886973, 342324171, 337726115, 1253535879, 332229903, 329358934, 318922427, 338122459, 341526710, 332350069, 330811120, 298419608, 341013694, 1253848111, 331851039, 335395898, 321467374, 345434253, 336184305, 337757709, 338371215, 336034019, 340656602, 333335840, 324427793, 1246285743, 1233637746, 330459345, 335425312, 292761942, 322416493, 333540084, 282004345, 1220841125, 336703663, 334606347, 331091377, 335715017, 315119041, 338100413, 339226044, 332044882, 334157879, 290304117, 335706187, 344156824, 333569251, 338110955, 336209766, 338273670, 339011770, 340534089, 328244468, 341533067];
http2Time = [331888584, 341292549, 348084183, 333329474, 336519459, 314235148, 346592260, 335788617, 1215190927, 1208657551, 1198349753, 328884552, 335831784, 329322101, 336655871, 309533461, 339471166, 300954452, 328733509, 333290964, 329694618, 331485338, 315943017, 333491782, 1412642402, 337531214, 1206094432, 329434301, 336286431, 292786039, 330768762, 326782568, 328994066, 342220448, 335658429, 338159949, 337179312, 327139526, 335876192, 334039944, 340050574, 342769190, 326468300, 326652890, 335056248, 315979903, 304013776, 1231488119, 332928875, 331571802, 335307282, 1305349050, 328563877, 338315694, 329472819, 337862957, 327256360, 322605652, 303906117, 334314236, 331292190, 1208513081, 332983329, 329525773, 347130303, 331038806, 342389493, 341992543, 338498141, 342025111, 326637456, 346428283, 324194205, 1213016619, 1217362386, 344929944, 329395005, 327618174, 328610348, 309858735, 339157543, 1380498912, 336266130, 340234215, 274622931, 331542533, 324637805, 349822025, 315854033, 316978125, 324209184, 289593967, 339716837, 332460249, 328915219, 333222629, 326641875, 328971968, 332831700, 334359629, 329838173, 338378064];

http1Time = http1Time / 1000000000;
http2Time = http2Time / 1000000000;

set(gca,'fontsize',14)

hold on
p1 = cdfplot(http1Time);
p2 = cdfplot(http2Time);
p1.LineWidth = 1;
p2.LineWidth = 1;
xlim([0 0.8])
xlabel('time(s)')
ylabel('CDF')
legend('HTTP/1.x', 'HTTP/2')
title('page transfer time')