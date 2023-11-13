from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import locale
import base64
from io import BytesIO

def generate_service_order_pdf(order_data, mec_name):
    # Configurar o locale para formatação de moeda
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    buffer = BytesIO()

    document = SimpleDocTemplate(buffer, pagesize=letter)

    # Cores
    dark_blue = colors.HexColor('#001F3F')  # Azul escuro
    light_blue = colors.HexColor('#7FDBFF')  # Azul claro

    # Criar estilos
    styles = getSampleStyleSheet()
    body_style = styles['BodyText']
    dark_blue_style = ParagraphStyle(
        'DarkBlueStyle',
        parent=body_style,
        textColor=dark_blue,
        spaceAfter=12,
    )
    light_blue_style = ParagraphStyle(
        'LightBlueStyle',
        parent=body_style,
        textColor=light_blue,
        spaceAfter=12,
    )
    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Heading1'],
        textColor=dark_blue,
        alignment=1,  # 0=left, 1=center, 2=right
        spaceAfter=12,
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
    client_table_data = [
        ["Cliente", ""],
        ["Nome", order_data['client']['name']],
        ["Email", order_data['client']['email']],
        ["Telefone", order_data['client']['phone']],
        ["Endereço", order_data['client']['address']],
        ["CPF", order_data['client']['document']],
    ]

    client_table = Table(client_table_data, colWidths=[4 * inch, 4 * inch])
    client_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), dark_blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (0, -1), light_blue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    content.append(client_table)
    content.append(Spacer(1, 12))  # Espaço

    # Adicionar veículo
    vehicle_data = [
        ["Veículo", ""],
        ["Marca/Modelo", f"{order_data['vehicle']['brand']} {order_data['vehicle']['model']}"],
        ["Placa", order_data['vehicle']['plate']],
        ["Cor", order_data['vehicle']['color']],
        ["Ano de Fabricação", order_data['vehicle']['fabrication_year']],
        ["Tipo", order_data['vehicle']['type']],
    ]

    vehicle_table = Table(vehicle_data, colWidths=[4 * inch, 4 * inch])
    vehicle_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), dark_blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
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
            price_formatted = locale.currency(price, grouping=True)
            services_data.append([service['service']['name'], price_formatted])

        # Adicionar linha de Valor Total para serviços
        services_data.append(["Valor Total", locale.currency(total_services_price, grouping=True)])
    else:
        # Adicionar linha de Valor Total mesmo se não houver serviços
        services_data.append(["Valor Total", locale.currency(0.0, grouping=True)])

    # Ajuste da largura da coluna
    services_table = Table(services_data, colWidths=[4 * inch, 4 * inch])  # Ajuste na largura da coluna
    services_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), dark_blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (0, -1), light_blue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    content.append(services_table)
    content.append(Spacer(1, 12))

    # Adicionar produtos
    products_data = [
        ["Produtos", "Quantidade", "Preço Unitário", "Preço Total"]
    ]

    # Adicionar produtos à tabela, se houver algum
    total_products_price = 0.0
    if order_data['products']:
        for product in order_data['products']:
            quantity = product['quantity']
            price_unit = locale.currency(product['product']['price'], grouping=True)
            price_total = locale.currency(quantity * product['product']['price'], grouping=True)
            products_data.append([product['product']['name'], str(quantity), price_unit, price_total])
            total_products_price += float(quantity) * product['product']['price']

        # Adicionar linha de Valor Total para produtos
        products_data.append(["", "", "Valor Total", locale.currency(total_products_price, grouping=True)])
    else:
        # Adicionar linha de Valor Total mesmo se não houver produtos
        products_data.append(["", "", "Valor Total", locale.currency(0.0, grouping=True)])

    products_table = Table(products_data, colWidths=[5 * inch, inch, inch, inch])
    products_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), dark_blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (0, -1), light_blue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    content.append(products_table)
    content.append(Spacer(1, 12))  # Espaço

    if order_data.get('comments'):
        comments_text = order_data['comments']
        comments_paragraph = Paragraph(f"<b>Observações:</b> {comments_text}", styles['Normal'])
        content.append(comments_paragraph)
        content.append(Spacer(1, 12))  # Espaço

    # Adicionar rodapé com o status
    footer = f"<b>Ordem de Serviço #{order_data['id']}</b><br/><b>Status:</b> {order_data.get('status', 'N/A')}"
    content.append(Paragraph(footer, styles['Heading4']))

    # Adicionar conteúdo ao PDF
    document.build(content)

    pdf_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Retorna a representação base64 do PDF
    return pdf_base64