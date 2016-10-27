load('resources/tcp_traffic_ratio.mat')

hold on

p1 = cdfplot(http1_request_ratios);
p2 = cdfplot(http2_request_ratios);
p3 = cdfplot(http1_response_ratios);
p4 = cdfplot(http2_response_ratios);

xlim([0.9 1.9])
p1.LineWidth = 1;
p2.LineWidth = 1;
p3.LineWidth = 1;
p4.LineWidth = 1;

ylabel('CDF')
xlabel('TCP retransmission ratio')
title('TCP retransmission ratio distribution')
legend('HTTP/1.x request', 'HTTP/2 request', 'HTTP/1.x response', 'HTTP/2 response')