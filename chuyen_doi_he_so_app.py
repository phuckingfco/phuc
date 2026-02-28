import streamlit as st

#  Đổi tên trên tab trình duyệt và icon
st.set_page_config(
    page_title="Ứng dụng của Hoàng Phúc", 
    page_icon="🔢",
    layout="centered"
)

#  Xóa menu "Made with Streamlit" 
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    /* Ép nền tối toàn trang */
    .stApp {
        background-color: #0E1117;
    }
    /* Chỉnh ô nhập liệu sang màu xám nhẹ */
    .stTextInput > div > div > input {
        background-color: #262730 !important;
        color: white !important;
        border: 1px solid #4CAF50 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* 1. Ép toàn bộ nền App và Sidebar luôn theo phong cách Dark Mode */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)), 
                    url("https://raw.githubusercontent.com/phuckingfco/binary-converter/main/z7232853078743_5002e1f2937a75093669037c322e7c09.jpg");
        background-size: cover;
        background-attachment: fixed;
    }

    /* 2. Sửa lỗi Sidebar bị trắng: Ép Sidebar luôn có màu tối */
    [data-testid="stSidebar"] {
        background-color: #111111 !important;
    }
    
    /* 3. Ép tất cả chữ trong Sidebar phải là màu trắng để nổi bật */
    [data-testid="stSidebar"] .main .block-container, 
    [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: white !important;
    }

    /* 4. Giữ khung nội dung chính luôn dễ đọc */
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.1); 
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* 5. Đảm bảo chữ ở nội dung chính luôn trắng và có bóng đổ */
    h1, h2, h3, p, span, label {
        color: #FFFFFF !important;
        text-shadow: 2px 2px 4px #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 1. Cấu hình trang
st.set_page_config(page_title="Bộ Chuyển Đổi Số - Hoàng Phúc", page_icon="🔢")

# 2. Cấu hình giao diện (Làm tối nền)
st.markdown(
    """
    <style>
    .stApp {
        /* Phủ một lớp gradient đen mờ lên trên ảnh nền */
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url("https://img.freepik.com/free-vector/abstract-binary-code-techno-background_1048-12836.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
    
    /* Làm cho khung nội dung chính hơi tối nhẹ nhưng vẫn đủ tương phản với chữ trắng */
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.5); /* Nền khung màu đen mờ 50% */
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1); /* Viền mờ cho khung thêm sang */
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        margin-top: 30px;
    }

    /* Đổi toàn bộ chữ sang màu trắng hoặc màu sáng để nổi bật trên nền tối */
    h1, h2, h3, p, span, label {
        color: #FFFFFF !important;
        text-shadow: 1px 1px 2px black; /* Thêm bóng cho chữ để dễ đọc hơn nữa */
    }

    /* Tùy chỉnh các ô nhập liệu cho hợp với tông tối */
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Tiêu đề chính
st.title("🔢 Ứng dụng Chuyển đổi Hệ số")
st.sidebar.title("🚀 Chủ sở hữu")
st.sidebar.write("Tác giả: **Hoàng Phúc**")
st.sidebar.caption("Phiên bản chuyên nghiệp 2026")


# 4. Chia các Tab chức năng
tab1, tab2, tab3 = st.tabs(["➡️ Sang Nhị Phân", "⬅️ Sang Thập Phân", "🔠 Sang Chữ Cái"])

with tab1:
        st.header("Đổi Số/Chữ sang Nhị Phân")
        with st.container(border=True):
            du_lieu = st.text_input("Nhập vào số hoặc chữ:", key="input1", placeholder="Ví dụ: 36 hoặc Thanh Hoa")
            
            if du_lieu:
                if du_lieu.isdigit():
                    # --- TRƯỜNG HỢP NHẬP SỐ ---
                    so = int(du_lieu)
                    ket_qua = bin(so).replace('0b', '')
                    st.markdown(f"""
                        <div style="background-color: #2b2b2b; padding: 15px; border-radius: 10px; border: 1px solid #555; width: calc(100% + 2px); margin-left: -1px;">
                            <span style="color: #4CAF50; font-weight: bold;">🔢 Kết quả nhị phân:</span>
                            <code style="color: white; font-size: 20px;">{ket_qua}</code>
                        </div>
                    """, unsafe_allow_html=True)
                
                else:
                    # --- TRƯỜNG HỢP NHẬP CHỮ (XỬ LÝ DỮ LIỆU TRƯỚC) ---
                    # Bước 1: Tạo danh sách nhị phân 
                    danh_sach_nhi_phan = []
                    for ky_tu in du_lieu:
                        ma_np = format(ord(ky_tu), '08b')
                        danh_sach_nhi_phan.append(ma_np)

                   
                    # --- 1. CÀI ĐẶT GIAO DIỆN (Chỉnh ở đây để máy tự nhớ, không hiện chữ thừa) ---
                    DO_CAO = "0px"          # 0px là mỏng nhất, 2px là mỏng vừa
                    MAU_CHU = "white"       # Ép chữ mã nhị phân luôn màu trắng
                    KHOANG_CACH_KHUNG = "2px" # Khoảng cách giữa các dòng ký tự
                    
                    # --- 2. HIỂN THỊ TỪNG KÝ TỰ ---
                    st.info(f"Mã nhị phân từng ký tự của '{du_lieu}':")
                    for ky_tu, ma_np in zip(du_lieu, danh_sach_nhi_phan):
                        st.markdown(f"""
                            <div style="
                                background-color: #2b2b2b; 
                                padding: {DO_CAO} 12px; 
                                border-radius: 6px; 
                                border: 1px solid #444; 
                                margin-bottom: {KHOANG_CACH_KHUNG}; 
                                width: fit-content;
                                display: flex;
                                align-items: center;
                                gap: 10px;">
                                <span style="color: #4CAF50; font-weight: bold; font-size: 14px;">{ky_tu} :</span> 
                                <code style="
                                    color: {MAU_CHU} !important; 
                                    background: transparent; 
                                    border: none;
                                    font-size: 14px;
                                    font-family: monospace;">
                                    {ma_np}
                                </code>
                            </div>
                        """, unsafe_allow_html=True)

                    # --- 3. HIỂN THỊ NGUYÊN CÂU 
                    st.markdown("---")
                    ket_qua_nguyen_cau = " ".join(danh_sach_nhi_phan)
                    st.markdown(f"""
                        <div style="
                            background-color: #2b2b2b; 
                            padding: 10px 15px; 
                            border-radius: 10px; 
                            border: 1px solid #555;">
                            <span style="color: #4CAF50; font-weight: bold; font-size: 14px;">✨ Kết quả nguyên câu:</span>
                            <br>
                            <code style="
                                color: {MAU_CHU} !important; 
                                font-size: 16px; 
                                background: transparent;
                                word-break: break-all;">
                                {ket_qua_nguyen_cau}
                            </code>
                        </div>
                    """, unsafe_allow_html=True)


# --- TAB 2: NHỊ PHÂN SANG THẬP PHÂN ---
with tab2:
    st.header("Đổi Nhị Phân sang Thập Phân")
    with st.container(border=True):
        nhi_phan = st.text_input("Nhập mã nhị phân (0 và 1):", key="input2", placeholder="Ví dụ: 101010")
        if nhi_phan:
            try:
                # 1. Chuyển đổi
                so_thap_phan = int(nhi_phan, 2)
                
                # 2. Định dạng khoảng trắng giữa hàng nghìn (187 627 066)
                so_dinh_dang = "{:,}".format(so_thap_phan).replace(",", " ") 
                
                st.markdown("---")
                st.success("Đã xử lý xong!")
                st.balloons()
                # --- PHẦN HIỂN THỊ KẾT QUẢ DÀI BẰNG KHUNG XANH ---
                st.markdown(f"""
                    <div style="
                        background-color: #111111; 
                        padding: 15px 20px; 
                        border-radius: 8px; 
                        border: 1px solid #333;
                        margin-bottom: 10px;
                        /* Hai dòng dưới đây giúp bảng dài bằng khung xanh */
                        display: flex; 
                        justify-content: flex-start;
                        align-items: center;
                        gap: 15px;">
                        <span style="color: #4CAF50; font-size: 14px; font-weight: bold; white-space: nowrap;">🔢 Kết quả:</span>
                        <span style="color: white; font-size: 24px; font-family: sans-serif; font-weight: bold; word-break: break-all;">
                            {so_dinh_dang}
                        </span>
                    </div>
                """, unsafe_allow_html=True)
                
            
            except ValueError:
                st.error("⚠️ Chỉ nhập 0 và 1 thôi Phúc nhé!")
                
# --- TAB 3: NHỊ PHÂN SANG CHỮ CÁI ---
with tab3:
    st.header("Đổi Nhị Phân sang Chữ cái")
    with st.container(border=True):
        input_nhi_phan = st.text_input("Nhập dãy nhị phân (cách nhau bằng khoảng trắng):", 
                                        key="input3", 
                                        placeholder="Ví dụ: 01010100 01001000")
        
        if input_nhi_phan:
            try:
                # Chuyển đổi nguyên chuỗi
                danh_sach = input_nhi_phan.split()
                chu_ket_qua = "".join([chr(int(b, 2)) for b in danh_sach])
                
               
                 # Hiển thị kết quả nguyên câu
                st.success("✨ Chữ cái tương ứng là:")
                # Tạo khung đen bằng Markdown + HTML
                st.markdown(f"""
                    <div style="background-color: #1a1a1a; color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #333; font-family: monospace; font-size: 20px;">
                        {chu_ket_qua}
                    </div>
                    """, unsafe_allow_html=True)
                
            except Exception:
                st.error("⚠️ Lỗi: Dãy nhị phân không đúng định dạng hoặc chứa ký tự lạ!")


# 5. Chân trang
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center;'>
        <p style='color: #FF4B4B; font-weight: bold; font-size: 20px;'>
            🚀 Thiết kế bởi Hoàng Phúc 🚀
        </p>
        <p style='color: gray;'>Bản quyền thuộc về PhucKing © 2026</p>
    </div>
    """, 
    unsafe_allow_html=True
)
