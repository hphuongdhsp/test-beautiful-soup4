# Hướng dẫn sủ dụng gói thư viện **beautiful soup** trong Python để **Web Scraping**

Nội dung của bài viết nhằm hướng dẫn các bạn mới làm quen với đào ảnh từ internet bằng gói thư viện beautiful soup. 

Bài viết gồm các ý chính chính sau:

## Outline

- <a href='#1'>1. Giới thiệu về Web Scaping</a>

- <a href='#2'>2. Tổng quan cấu trúc web </a>  
    - <a id='#2-1'>2.1. HTML, CSS </a> 
    - <a id='#2-1'>2.2. Cấu trúc web  </a> 

- <a href='#3'>3. Bài toán cụ thể: craping ảnh từ trang web: http://www.globalskinatlas.com/diagindex.cfm </a>
    - <a id='#3-1'>3.1. Cấu trúc của trang web  </a>
    - <a id='#3-2'>3.2. Cách download ảnh thủ công </a> 
    - <a id='#3-2'>3.3. Xây dựng thuật toán từ thác tác down ảnh thủ công  </a> 
- <a href='#4'>4. Giới thiệu gói thư viện beautiful soup </a>
    - <a id='#4-1'>3.1.  </a>
    - <a id='#4-2'>3.2. Xây dựng mô hình</a> 

- <a href='#4'>5. Hoàn thành code </a>
    - <a id='#4-1'>3.1.  </a>
    - <a id='#4-2'>3.2. Xây dựng mô hình</a> 


# <a id='1'>1.Giới thiệu về Web Scaping</a>

Internet có nguồn dữ liệu khổng lồ, dữ liệu mà chúng ta hoàn toàn có thể truy cập bằng cách sử dụng web cùng một công cụ lập trình (Python, C++). Web Scaping là tác vụ download tất cả thông tin liên quan từ một trang web cố định. Ví dụ chúng ta muốn download tất cả các ảnh từ trang web http://www.globalskinatlas.com/diagindex.cfm để làm phong phú kho dữ liệu. 

Một số trang web cung cấp cho chúng ta thông qua một API (Application Programming Interface), một số trang web khác có thể co ngừoi dùng lấy dữ liệu thông qua database có sẵn. Ví dụ khi bạn muốn download ảnh từ một trang web, bạn click vào ảnh trên website, từ website sẽ đưa bạn tới một trang web khác, nơi đó có lưu trữ ảnh trực tiếp trên server. 

# <a id='2'>2. Tổng quan cấu trúc web</a>

Trước khi đi sâu vào làm sao có thể download tất cả dữ liệu từ một trang web, chúng ta sẽ tìm hiểu cấu trúc của một trang web. Việc này giống như đi câu cá, bạn tìm hiểu cấu trúc của hồ nước, để có thêm thông tin giúp việc câu cá dễ dàng hơn. 


## <a id='2.1'>2. Tổng quan HTML, CSS</a>

Khi chúng ta truy cập một trang web, trình duyệt web (Firefox, Chrome) đưa ra yêu cầu đến máy chủ của trang web. Yêu cầu này được gọi là yêu cầu GET, sau đó chúng ta nhận được thông tin từ máy chủ. Nguồn thông tin từ máy chủ sẽ vẫn được trả lại thông tin gồm những tập file. Nhờ trình duyệt web, các tập này sẽ hiển thị dứoi dạng web. Cấu thành của tập để trình duyệt web có thể đọc một trang web bao gồm:

HTML - nội dung chính của trang.
CSS - File này hỗ trợ HTML để hiển thi web đẹp hơn.
JS - Các tệp Javascript thêm tính tương tác cho các trang web.
Hình ảnh - các định dạng hình ảnh, chẳng hạn như JPG và PNG, cho phép các trang web hiển thị hình ảnh.
Sau khi trình duyệt của chúng tôi nhận được tất cả các tệp, nó sẽ hiển thị trang và hiển thị cho chúng tôi.

Ví dụ: Khi chúng ta vào trình duyệt Chrome, chúng ta muốn try tập vào trang http://www.globalskinatlas.com/diagindex.cfm , khi đó máy chủ sẽ trả lại một tập, tập dữ liệu này gồm các file (html, css, javascript,), các file này sẽ được gửi trực tiếp về Chrome, thông qua trình duyệt, tất cả các tệp này sẽ tạp nên một trang web.  

Để hiểu rõ cấu trúc một trang web, chúng ta sẽ tìm hiểu sâu file HTML. Ở các trình duyệt. Để hiển thị cấu trúc file HTML, chúng ta bấm phím *F12*. 

## <a id='2.1'>2. Tổng quan HTML, CSS</a>

