from pathlib import Path

base = Path('C:/Users/Admin/Downloads/TIEU_LUAN_SoAD/figures')
base.mkdir(parents=True, exist_ok=True)

def write_svg_sketchy(name, w, h, body):
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="background-color: #FDFBF7;">
<defs>
    <pattern id="dotGrid" x="0" y="0" width="24" height="24" patternUnits="userSpaceOnUse">
        <circle cx="2" cy="2" r="1.5" fill="#d1d5db" opacity="0.5"/>
    </pattern>

    <filter id="sketch" x="-10%" y="-10%" width="120%" height="120%">
        <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="3" result="noise" />
        <feDisplacementMap in="SourceGraphic" in2="noise" scale="2.5" xChannelSelector="R" yChannelSelector="G" />
    </filter>

    <marker id="arrowhead" markerWidth="8" markerHeight="8" refX="6.5" refY="4" orient="auto">
        <path d="M 0 1 L 6.5 4 L 0 7 Q 2.5 4 0 1" fill="#1e293b" />
    </marker>

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&amp;display=swap');
        text {{ font-family: 'Kalam', 'Comic Sans MS', cursive; }}
        
        /* Chỉnh lại toàn bộ text sang màu tối (mực bút bi/bút lông) */
        .title {{ font-size: 32px; font-weight: 700; fill: #0f172a; filter: url(#sketch); }}
        .subtitle {{ font-size: 18px; font-weight: 400; fill: #475569; filter: url(#sketch); }}
        
        .text-light {{ font-size: 18px; font-weight: 700; fill: #0f172a; }}
        .small-light {{ font-size: 14px; font-weight: 400; fill: #334155; }}
        
        .text-dark {{ font-size: 18px; font-weight: 700; fill: #0f172a; }}
        .small-dark {{ font-size: 14px; font-weight: 400; fill: #334155; }}
        
        /* Khung viền đứt nét, hơi nguệch ngoạc */
        .box {{ fill: rgba(255, 255, 255, 0.4); stroke: #475569; stroke-width: 2.5; stroke-dasharray: 8 4; rx: 8; filter: url(#sketch); }}
        
        /* Các Node sử dụng màu Pastel giống màu bút dạ quang, viền mực đen nét run */
        .node-blue {{ fill: #bae6fd; stroke: #0f172a; stroke-width: 2; rx: 6; filter: url(#sketch); }}
        .node-green {{ fill: #bbf7d0; stroke: #0f172a; stroke-width: 2; rx: 6; filter: url(#sketch); }}
        .node-purple {{ fill: #e9d5ff; stroke: #0f172a; stroke-width: 2; rx: 6; filter: url(#sketch); }}
        .node-coral {{ fill: #fecdd3; stroke: #0f172a; stroke-width: 2; rx: 6; filter: url(#sketch); }}
        .node-dark {{ fill: #e2e8f0; stroke: #0f172a; stroke-width: 2; rx: 6; filter: url(#sketch); }}

        /* Database mô phỏng nét vẽ trụ */
        .db-blue {{ fill: #bae6fd; stroke: #0f172a; stroke-width: 2; filter: url(#sketch); }}
        .db-purple {{ fill: #e9d5ff; stroke: #0f172a; stroke-width: 2; filter: url(#sketch); }}
        .db-green {{ fill: #bbf7d0; stroke: #0f172a; stroke-width: 2; filter: url(#sketch); }}
        .db-coral {{ fill: #fecdd3; stroke: #0f172a; stroke-width: 2; filter: url(#sketch); }}
        .db-top {{ fill: rgba(255,255,255,0.3); stroke: #0f172a; stroke-width: 2; filter: url(#sketch); }}
        
        /* Đường kẻ và mũi tên mô phỏng nét bút bi */
        .line-solid {{ stroke: #1e293b; stroke-width: 2.5; fill: none; stroke-linecap: round; filter: url(#sketch); }}
        .arrow {{ stroke: #1e293b; stroke-width: 2.5; fill: none; stroke-linecap: round; marker-end: url(#arrowhead); filter: url(#sketch); }}
        .dashed {{ stroke: #1e293b; stroke-width: 2.5; fill: none; stroke-linecap: round; stroke-dasharray: 8 6; marker-end: url(#arrowhead); filter: url(#sketch); }}
    </style>
</defs>

<rect width="100%" height="100%" fill="#FDFBF7"/>

{body}
</svg>'''
    (base / name).write_text(content, encoding='utf-8')

# 1. Monolithic Architecture
write_svg_sketchy('chapter1_monolithic_architecture.svg', 900, 450, '''
<rect x="95" y="75" width="710" height="230" class="box"/>
<text x="450" y="115" text-anchor="middle" class="subtitle">Ứng dụng nguyên khối</text>

<rect x="135" y="145" width="180" height="90" class="node-blue"/>
<text x="225" y="190" text-anchor="middle" class="text-light">Presentation</text><text x="225" y="215" text-anchor="middle" class="small-light">UI / API</text>

<rect x="360" y="145" width="180" height="90" class="node-purple"/>
<text x="450" y="190" text-anchor="middle" class="text-light">Business Logic</text><text x="450" y="215" text-anchor="middle" class="small-light">Nghiệp vụ</text>

<rect x="585" y="145" width="180" height="90" class="node-green"/>
<text x="675" y="190" text-anchor="middle" class="text-light">Data Access</text><text x="675" y="215" text-anchor="middle" class="small-light">Truy cập dữ liệu</text>

<path d="M320 190 L352 190" class="arrow"/>
<path d="M545 190 L577 190" class="arrow"/>
<path d="M675 240 C675 300,575 318,455 342" class="arrow"/>
<path d="M330 350 C330 335,570 335,570 350 L570 390 C570 405,330 405,330 390 Z" class="db-coral"/>
<path d="M330 350 C330 365,570 365,570 350" class="db-top"/>
<text x="450" y="385" text-anchor="middle" class="text-light">Cơ sở dữ liệu dùng chung</text>
''')

# 2. E-Commerce Monolithic
write_svg_sketchy('chapter1_ecommerce_monolith.svg', 900, 450, '''
<rect x="75" y="75" width="750" height="230" class="box"/>
<text x="450" y="115" text-anchor="middle" class="subtitle">Một codebase - một gói triển khai</text>

<rect x="105" y="145" width="95" height="80" class="node-blue"/><text x="152" y="185" text-anchor="middle" class="text-light">Product</text><text x="152" y="210" text-anchor="middle" class="small-light">Module</text>
<rect x="225" y="145" width="95" height="80" class="node-purple"/><text x="272" y="185" text-anchor="middle" class="text-light">User</text><text x="272" y="210" text-anchor="middle" class="small-light">Module</text>
<rect x="345" y="145" width="95" height="80" class="node-coral"/><text x="392" y="185" text-anchor="middle" class="text-light">Cart</text><text x="392" y="210" text-anchor="middle" class="small-light">Module</text>
<rect x="465" y="145" width="95" height="80" class="node-green"/><text x="512" y="185" text-anchor="middle" class="text-light">Order</text><text x="512" y="210" text-anchor="middle" class="small-light">Module</text>
<rect x="585" y="145" width="95" height="80" class="node-dark"/><text x="632" y="185" text-anchor="middle" class="text-light">Payment</text><text x="632" y="210" text-anchor="middle" class="small-light">Module</text>
<rect x="705" y="145" width="95" height="80" class="node-blue"/><text x="752" y="185" text-anchor="middle" class="text-light">Shipping</text><text x="752" y="210" text-anchor="middle" class="small-light">Module</text>

<path d="M152 230 C152 305,285 318,390 342" class="dashed"/>
<path d="M272 230 C272 300,355 318,420 342" class="dashed"/>
<path d="M392 230 C400 278,415 312,430 342" class="dashed"/>
<path d="M512 230 C505 278,488 312,470 342" class="dashed"/>
<path d="M632 230 C632 300,545 318,485 342" class="dashed"/>
<path d="M752 230 C752 305,615 318,510 342" class="dashed"/>
<text x="450" y="285" text-anchor="middle" class="small-dark">dùng chung dữ liệu</text>
<path d="M330 350 C330 335,570 335,570 350 L570 390 C570 405,330 405,330 390 Z" class="db-coral"/>
<path d="M330 350 C330 365,570 365,570 350" class="db-top"/>
<text x="450" y="385" text-anchor="middle" class="text-light">Một cơ sở dữ liệu</text>
''')

# 3. Microservices Architecture
write_svg_sketchy('chapter1_microservices_architecture.svg', 950, 520, '''

<rect x="380" y="70" width="190" height="60" class="node-dark"/>
<text x="475" y="105" text-anchor="middle" class="text-light">API Gateway</text>

<path d="M475 135 L475 158" class="arrow"/>
<path d="M170 165 L780 165" class="line-solid"/>

<path d="M170 172 L170 198" class="arrow"/><rect x="95" y="205" width="150" height="65" class="node-blue"/><text x="170" y="243" text-anchor="middle" class="text-light">Product Service</text>
<path d="M170 277 L170 312" class="arrow"/><path d="M100 320 C100 305,240 305,240 320 L240 370 C240 385,100 385,100 370 Z" class="db-blue"/><path d="M100 320 C100 335,240 335,240 320" class="db-top"/><text x="170" y="360" text-anchor="middle" class="text-light">Product DB</text>

<path d="M370 172 L370 198" class="arrow"/><rect x="295" y="205" width="150" height="65" class="node-purple"/><text x="370" y="243" text-anchor="middle" class="text-light">User Service</text>
<path d="M370 277 L370 312" class="arrow"/><path d="M300 320 C300 305,440 305,440 320 L440 370 C440 385,300 385,300 370 Z" class="db-purple"/><path d="M300 320 C300 335,440 335,440 320" class="db-top"/><text x="370" y="360" text-anchor="middle" class="text-light">User DB</text>

<path d="M580 172 L580 198" class="arrow"/><rect x="505" y="205" width="150" height="65" class="node-green"/><text x="580" y="243" text-anchor="middle" class="text-light">Order Service</text>
<path d="M580 277 L580 312" class="arrow"/><path d="M510 320 C510 305,650 305,650 320 L650 370 C650 385,510 385,510 370 Z" class="db-green"/><path d="M510 320 C510 335,650 335,650 320" class="db-top"/><text x="580" y="360" text-anchor="middle" class="text-light">Order DB</text>

<path d="M780 172 L780 198" class="arrow"/><rect x="705" y="205" width="150" height="65" class="node-coral"/><text x="780" y="243" text-anchor="middle" class="text-light">Payment Service</text>
<path d="M780 277 L780 312" class="arrow"/><path d="M710 320 C710 305,850 305,850 320 L850 370 C850 385,710 385,710 370 Z" class="db-coral"/><path d="M710 320 C710 335,850 335,850 320" class="db-top"/><text x="780" y="360" text-anchor="middle" class="text-light">Payment DB</text>

<path d="M505 222 C425 162,325 162,245 222" class="dashed"/><text x="375" y="155" text-anchor="middle" class="small-dark">API / Event</text>
<path d="M655 222 C675 162,705 162,705 222" class="dashed"/><text x="680" y="155" text-anchor="middle" class="small-dark">API / Event</text>
<path d="M245 254 C330 302,420 302,505 254" class="dashed"/>
<path d="M655 254 C675 302,705 302,705 254" class="dashed"/>
''')

# 4. Monolith vs Microservices
write_svg_sketchy('chapter1_monolith_vs_microservices.svg', 950, 500, '''

<rect x="60" y="75" width="360" height="260" class="box"/>
<text x="240" y="115" text-anchor="middle" class="text-dark">Monolithic</text>
<rect x="100" y="145" width="280" height="115" class="node-dark"/>
<text x="240" y="185" text-anchor="middle" class="text-light">Product | User | Order</text>
<text x="240" y="225" text-anchor="middle" class="text-light">Payment | Shipping</text>
<path d="M240 260 L240 300" class="arrow"/>
<path d="M160 300 C160 285,320 285,320 300 L320 340 C320 355,160 355,160 340 Z" class="db-coral"/>
<path d="M160 300 C160 315,320 315,320 300" class="db-top"/>
<text x="240" y="332" text-anchor="middle" class="text-light">CSDL dùng chung</text>

<rect x="530" y="75" width="360" height="330" class="box"/>
<text x="710" y="115" text-anchor="middle" class="text-dark">Microservices</text>
<rect x="570" y="145" width="120" height="55" class="node-blue"/><text x="630" y="178" text-anchor="middle" class="text-light">Product Svc</text>
<rect x="730" y="145" width="120" height="55" class="node-purple"/><text x="790" y="178" text-anchor="middle" class="text-light">User Svc</text>
<rect x="570" y="255" width="120" height="55" class="node-green"/><text x="630" y="288" text-anchor="middle" class="text-light">Order Svc</text>
<rect x="730" y="255" width="120" height="55" class="node-coral"/><text x="790" y="288" text-anchor="middle" class="text-light">Payment Svc</text>
<path d="M630 200 L630 225" class="arrow"/><text x="630" y="240" text-anchor="middle" class="small-dark">DB riêng</text>
<path d="M790 200 L790 225" class="arrow"/><text x="790" y="240" text-anchor="middle" class="small-dark">DB riêng</text>
<path d="M630 310 L630 335" class="arrow"/><text x="630" y="350" text-anchor="middle" class="small-dark">DB riêng</text>
<path d="M790 310 L790 335" class="arrow"/><text x="790" y="350" text-anchor="middle" class="small-dark">DB riêng</text>
<path d="M690 173 L730 173" class="dashed"/>
<path d="M690 283 L730 283" class="dashed"/>
<path d="M630 200 C630 230,630 230,630 255" class="dashed"/>
<path d="M790 200 C790 230,790 230,790 255" class="dashed"/>
''')

# 5. DDD Flow
write_svg_sketchy('chapter1_ddd_flow.svg', 900, 360, '''

<rect x="70" y="120" width="155" height="75" class="node-dark"/><text x="147" y="153" text-anchor="middle" class="text-light">Business</text><text x="147" y="175" text-anchor="middle" class="small-light">Domain</text>
<rect x="275" y="120" width="155" height="75" class="node-blue"/><text x="352" y="153" text-anchor="middle" class="text-light">Domain</text><text x="352" y="175" text-anchor="middle" class="small-light">Model</text>
<rect x="480" y="120" width="155" height="75" class="node-purple"/><text x="557" y="153" text-anchor="middle" class="text-light">Bounded</text><text x="557" y="175" text-anchor="middle" class="small-light">Context</text>
<rect x="685" y="120" width="155" height="75" class="node-coral"/><text x="762" y="153" text-anchor="middle" class="text-light">Microservice</text><text x="762" y="175" text-anchor="middle" class="small-light">Service</text>

<path d="M225 158 L275 158" class="arrow"/><path d="M430 158 L480 158" class="arrow"/><path d="M635 158 L685 158" class="arrow"/>
<text x="450" y="265" text-anchor="middle" class="subtitle">DDD giúp chuyển tri thức nghiệp vụ thành ranh giới service rõ ràng.</text>
''')

# 6. Aggregate Example
write_svg_sketchy('chapter1_aggregate_example.svg', 900, 430, '''

<rect x="170" y="75" width="560" height="280" class="box"/>
<text x="450" y="115" text-anchor="middle" class="text-dark">Order Aggregate</text>

<rect x="225" y="145" width="180" height="70" class="node-purple"/><text x="315" y="176" text-anchor="middle" class="text-light">Order</text><text x="315" y="196" text-anchor="middle" class="small-light">Aggregate Root</text>
<rect x="500" y="145" width="170" height="70" class="node-blue"/><text x="585" y="176" text-anchor="middle" class="text-light">OrderItem</text><text x="585" y="196" text-anchor="middle" class="small-light">Entity</text>
<rect x="225" y="255" width="180" height="65" class="node-green"/><text x="315" y="292" text-anchor="middle" class="text-light">Money</text><text x="315" y="312" text-anchor="middle" class="small-light">Value Object</text>
<rect x="500" y="255" width="170" height="65" class="node-coral"/><text x="585" y="292" text-anchor="middle" class="text-light">Address</text><text x="585" y="312" text-anchor="middle" class="small-light">Value Object</text>

<path d="M405 180 L492 180" class="arrow"/>
<path d="M315 215 L315 247" class="arrow"/>
<path d="M405 190 C450 230,515 238,585 247" class="arrow"/>
<text x="450" y="238" text-anchor="middle" class="small-dark">quản lý nhất quán</text>
''')

# 7. Context Map E-Commerce
write_svg_sketchy('chapter1_context_map_ecommerce.svg', 950, 430, '''

<rect x="80" y="100" width="180" height="70" class="node-blue"/><text x="170" y="141" text-anchor="middle" class="text-light">Catalog Context</text>
<rect x="385" y="100" width="180" height="70" class="node-purple"/><text x="475" y="141" text-anchor="middle" class="text-light">Order Context</text>
<rect x="690" y="100" width="180" height="70" class="node-green"/><text x="780" y="141" text-anchor="middle" class="text-light">Payment Context</text>
<rect x="385" y="260" width="180" height="70" class="node-coral"/><text x="475" y="301" text-anchor="middle" class="text-light">Shipping Context</text>

<path d="M385 135 L260 135" class="arrow"/><text x="322" y="122" text-anchor="middle" class="small-dark">lấy thông tin SP</text>
<path d="M565 135 L690 135" class="arrow"/><text x="627" y="122" text-anchor="middle" class="small-dark">yêu cầu thanh toán</text>
<path d="M475 170 L475 260" class="dashed"/><text x="500" y="220" text-anchor="middle" class="small-dark">sự kiện giao hàng</text>
''')

# 8. Healthcare Decomposition
write_svg_sketchy('chapter1_healthcare_decomposition.svg', 1000, 560, '''

<rect x="405" y="55" width="190" height="55" class="node-dark"/><text x="500" y="88" text-anchor="middle" class="text-light">API Gateway</text>

<path d="M500 110 L500 145" class="arrow"/><path d="M145 145 L855 145" class="line-solid"/>

<path d="M145 145 L145 185" class="arrow"/><rect x="67" y="185" width="156" height="58" class="node-blue"/><text x="145" y="219" text-anchor="middle" class="text-light">Patient Service</text>
<path d="M322 145 L322 185" class="arrow"/><rect x="244" y="185" width="156" height="58" class="node-purple"/><text x="322" y="219" text-anchor="middle" class="text-light">Doctor Service</text>
<path d="M500 145 L500 185" class="arrow"/><rect x="422" y="185" width="156" height="58" class="node-coral"/><text x="500" y="219" text-anchor="middle" class="text-light">Appointment</text>
<path d="M678 145 L678 185" class="arrow"/><rect x="600" y="185" width="156" height="58" class="node-green"/><text x="678" y="219" text-anchor="middle" class="text-light">Medical Record</text>
<path d="M855 145 L855 185" class="arrow"/><rect x="777" y="185" width="156" height="58" class="node-dark"/><text x="855" y="219" text-anchor="middle" class="text-light">Billing Service</text>

<path d="M500 243 L500 300" class="arrow"/><rect x="415" y="300" width="170" height="58" class="node-purple"/><text x="500" y="335" text-anchor="middle" class="text-light">Prescription</text>

<path d="M422 232 C365 282,265 282,223 232" class="dashed"/><text x="320" y="296" text-anchor="middle" class="small-dark">API / Event</text>
<path d="M578 232 C635 282,735 282,777 232" class="dashed"/><text x="680" y="296" text-anchor="middle" class="small-dark">API / Event</text>
<path d="M585 329 C710 405,870 365,870 243" class="dashed"/>

<text x="500" y="440" text-anchor="middle" class="subtitle">Mỗi bounded context ánh xạ thành một microservice độc lập.</text>
''')

# 9. Service Relationships
write_svg_sketchy('chapter1_service_relationships.svg', 950, 430, '''

<rect x="80" y="75" width="170" height="65" class="node-blue"/><text x="165" y="114" text-anchor="middle" class="text-light">Patient Service</text>
<rect x="390" y="75" width="170" height="65" class="node-coral"/><text x="475" y="114" text-anchor="middle" class="text-light">Appointment</text>
<rect x="700" y="75" width="170" height="65" class="node-purple"/><text x="785" y="114" text-anchor="middle" class="text-light">Doctor Service</text>

<rect x="390" y="215" width="170" height="65" class="node-green"/><text x="475" y="254" text-anchor="middle" class="text-light">Medical Record</text>
<rect x="690" y="215" width="185" height="65" class="node-purple"/><text x="782" y="254" text-anchor="middle" class="text-light">Prescription</text>
<rect x="80" y="215" width="170" height="65" class="node-dark"/><text x="165" y="254" text-anchor="middle" class="text-light">Billing Service</text>

<path d="M390 108 L250 108" class="arrow"/><text x="320" y="96" text-anchor="middle" class="small-dark">xác nhận BN</text>
<path d="M560 108 L700 108" class="arrow"/><text x="630" y="96" text-anchor="middle" class="small-dark">xác nhận BS</text>
<path d="M475 140 L475 215" class="dashed"/><text x="520" y="182" text-anchor="middle" class="small-dark">hoàn thành khám</text>
<path d="M560 248 L690 248" class="arrow"/><text x="625" y="236" text-anchor="middle" class="small-dark">kê đơn</text>
<path d="M390 248 L250 248" class="arrow"/><text x="320" y="236" text-anchor="middle" class="small-dark">tính phí DV</text>
<path d="M690 280 C545 378,330 378,250 280" class="dashed"/><text x="475" y="378" text-anchor="middle" class="small-dark">tính phí đơn thuốc</text>
<path d="M475 140 C345 168,215 170,165 207" class="dashed"/><text x="290" y="166" text-anchor="middle" class="small-dark">tính phí lịch khám</text>
''')

print("Done: regenerated hand-drawn chapter 1 SVG figures.")