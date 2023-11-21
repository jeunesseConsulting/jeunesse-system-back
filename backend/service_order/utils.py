from babel.numbers import format_currency
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import base64
from io import BytesIO
import datetime

def format_currency_babel(value, currency='BRL'):
    return format_currency(value, currency, locale='pt_BR')

def generate_service_order_pdf(order_data, mec_name):
    buffer = BytesIO()
    document = SimpleDocTemplate(buffer, pagesize=letter)

        # Cores
    dark_blue = colors.HexColor('#0a3561')  # Azul escuro
    light_blue = colors.HexColor('#8eb8fa')  # Azul claro

        # Criar estilos
    styles = getSampleStyleSheet()
    body_style = styles['BodyText']
    dark_blue_style = ParagraphStyle(
        'DarkBlueStyle',
        parent=body_style,
        textColor=dark_blue,
        spaceAfter=12,
    )

    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Heading1'],
        textColor=dark_blue,
        alignment=1,  # 0=left, 1=center, 2=right
        spaceAfter=12,
        fontSize=26,
        fontName='Helvetica-Bold',
        italic=False,
    )

    comments_style = ParagraphStyle(
        'CommentsStyle',  # Escolha um nome único para o estilo
        parent=styles['Normal'],
        fontSize=12,  # Ajuste o tamanho da fonte conforme necessário
        spaceAfter=10,
    )

        # Criar conteúdo do PDF
    content = []

        # Adicionar número da ordem de serviço e nome do cliente
    order_number_and_client = mec_name
    content.append(Paragraph(order_number_and_client, header_style))
    content.append(Spacer(1, 12))  # Espaço

        # Adicionar uma linha de cor azul escuro
    content.append(Paragraph("", dark_blue_style))  # Caixa de cor azul escuro
    content.append(Spacer(1, 12))  # Espaço

        # Montar tabela com informações do cliente

    try:
        client_table_data = [
            ["Cliente", ""],
            ["Nome", order_data['client']['name']],
            ["Email", order_data['client']['email']],
            ["Telefone", order_data['client']['phone']],
            ["Endereço", order_data['client']['address']],
            ["CPF", order_data['client']['document']],
        ]
    except:
        try:
            name = order_data['client']['name']
        except:
            name = ""

        try:
            phone = order_data['client']['phone']
        except:
            phone = ""

        client_table_data = [
            ["Cliente", ""],
            ["Nome", name],
            ["Email", ""],
            ["Telefone", phone],
            ["Endereço", ""],
            ["CPF", ""],
        ]

    client_table = Table(client_table_data, colWidths=[4 * inch, 4 * inch])
    client_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), dark_blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (0, -1), light_blue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    content.append(client_table)
    content.append(Spacer(1, 12))  # Espaço

        # Adicionar veículo

    try:
        vehicle_data = [
            ["Veículo", ""],
            ["Marca/Modelo", f"{order_data['vehicle']['brand']} {order_data['vehicle']['model']}"],
            ["Placa", order_data['vehicle']['plate']],
            ["Cor", order_data['vehicle']['color']],
            ["Ano de Fabricação", order_data['vehicle']['fabrication_year']],
            ["Tipo", order_data['vehicle']['type']],
        ]
    except:
        try:
            model = order_data['vehicle']['model']
        except:
            model = ""

        try:
            year = order_data['vehicle']['fabrication_year']
        except:
            year = ""

        try:
            plate = order_data['vehicle']['plate']
        except:
            plate = ""

        vehicle_data = [
            ["Veículo", ""],
            ["Marca/Modelo", model],
            ["Placa", plate],
            ["Cor", ""],
            ["Ano de Fabricação", year],
            ["Tipo", ""],
        ]

    vehicle_table = Table(vehicle_data, colWidths=[4 * inch, 4 * inch])
    vehicle_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), dark_blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (0, -1), light_blue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    content.append(vehicle_table)
    content.append(Spacer(1, 12))  # Espaço

        # Adicionar serviços
    services_data = [
        ["Serviços", ""]
    ]

        # Adicionar serviços à tabela, se houver algum
    total_services_price = 0.0
    if order_data['services']:
        for service in order_data['services']:
            price = service['price']
            total_services_price += price
            price_formatted = format_currency_babel(price)
            services_data.append([service['service']['name'], price_formatted])

            # Adicionar linha de Valor Total para serviços
        services_data.append(["Valor Total", format_currency_babel(total_services_price)])
    else:
            # Adicionar linha de Valor Total mesmo se não houver serviços
        services_data.append(["Valor Total", format_currency_babel(0.0)])

        # Ajuste da largura da coluna
    services_table = Table(services_data, colWidths=[4 * inch, 4 * inch])  # Ajuste na largura da coluna
    services_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), dark_blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (0, -1), light_blue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    content.append(services_table)
    content.append(Spacer(1, 12))

        # Adicionar produtos
    products_data = [
        ["Produtos", "Quantidade", "UN","Preço Unitário", "Preço Total"]
    ]

        # Adicionar produtos à tabela, se houver algum
    total_products_price = 0.0
    if order_data['products']:
        for product in order_data['products']:
            quantity = product['quantity']
            price_unit = format_currency_babel(product['product']['price'])
            price_total = format_currency_babel(quantity * product['product']['price'])
            products_data.append([product['product']['name'], str(quantity), product['product']['measure_unit']['acronym'], price_unit, price_total])
            total_products_price += float(quantity) * product['product']['price']

            # Adicionar linha de Valor Total para produtos
        products_data.append(["Valor Total", "", "", "", format_currency_babel(total_products_price)])
    else:
            # Adicionar linha de Valor Total mesmo se não houver produtos
        products_data.append(["", "", "", "Valor Total", format_currency_babel(0.0)])

    sec_col = 1
    products_table = Table(products_data, colWidths=[4 * inch, sec_col * inch, sec_col * inch, sec_col * inch, sec_col * inch])
    products_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), dark_blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (0, -1), light_blue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    content.append(products_table)
    content.append(Spacer(1, 24))  # Espaço

    if order_data.get('comments'):
        comments_text = order_data['comments']
        comments_paragraph = Paragraph(f"<b>Observações:</b> {comments_text}", comments_style)
        content.append(comments_paragraph)
        content.append(Spacer(1, 12))  # Espaço

    try:
        created_at = datetime.datetime.strptime(order_data["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%d/%m/%Y")
    except:
        created_at = "N/A"
    created_paragraph = Paragraph(f'<b>Data de abertura da OS:</b> {created_at}', styles['Normal'])
    content.append(created_paragraph)

    try:
        if order_data['payment_method']:
            payment_method = order_data['payment_method']['name']
        else:
            payment_method = 'N/A'
    except:
        payment_method = 'N/A'

    payment_paragraph = Paragraph(f'<b>Método de pagamento:</b> {payment_method}')
    content.append(payment_paragraph)

    installments = order_data['installments']
    installments_paragraph = Paragraph(f'<b>Parcelas:</b> {installments}')
    content.append(installments_paragraph)

    try:
        if order_data["delivery_forecast"]:
            delivery_forecast = datetime.datetime.strptime(order_data["delivery_forecast"], "%Y-%m-%d").strftime("%d/%m/%Y")
        else:
            delivery_forecast = "N/A"
    except:
        delivery_forecast = "N/A"
            
    delivery_paragraph = Paragraph(f'<b>Previsão de entrega:</b> {delivery_forecast}', styles["Normal"])
    content.append(delivery_paragraph)

        # Adicionar rodapé com o status
    footer = f"<b>Ordem de Serviço #{order_data['id']}</b><br/><br/><b>Status:</b> {str(order_data.get('status', 'N/A')).upper()}"
    content.append(Paragraph(footer, styles['Heading4']))

        # Adicionar conteúdo ao PDF
    document.build(content)

    pdf_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        # Retorna a representação base64 do PDF
    return pdf_base64

