import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import pandas as pd

app = dash.Dash()

app.scripts.config.serve_locally = True
app.config['suppress_callback_exceptions'] = True

tabs_styles = {
    'height': '44px'
}

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}


def create_tab1():
    table1 = pd.read_csv('inputTables/tab1/input1.csv')
    table2 = pd.read_csv('inputTables/tab1/input2.csv')
    table3 = pd.read_csv('inputTables/tab1/input3.csv')
    table4 = pd.read_csv('inputTables/tab1/input4.csv')
    table5 = pd.read_csv('inputTables/tab1/input5.csv')
    return html.Div([
        html.Div([
            dcc.Dropdown(
                id='select_1',
                options=[
                    {'label': i, 'value': i} for i in ['A', 'B', 'C']
                ],
            ),
            html.Div([], id='select_next_1')],
            id='select_boxes'
        ),
        html.H4('Engagement Details'),
        dt.DataTable(
            rows=table1.to_dict('records'),
            columns=table1.columns,
            id='table_1'
        ),
        html.H4('Engagement Results Summary'),
        dt.DataTable(
            rows=table2.to_dict('records'),
            columns=table2.columns,
            id='table_2'
        ),
        html.H4('Engagement Exceptions'),
        dt.DataTable(
            rows=table3.to_dict('records'),
            columns=table3.columns,
            id='table_3'
        ),
        html.H4('Process Exceptions and Waivers'),
        dt.DataTable(
            rows=table4.to_dict('records'),
            columns=table4.columns,
            id='table_4'
        ),
        html.H4('Engagement Issues'),
        dt.DataTable(
            rows=table5.to_dict('records'),
            columns=table5.columns,
            id='table_5'
        ),
        html.H4('Notes'),
        dcc.Textarea(
            placeholder='Enter your Notes...',
            value='',
            style={'width': '100%'},
            id='table_6'
        ),
        html.Button('Download', id='button1', style={'margin-top': '10px'}),
        html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'}),
    ], id='tab_1',
        className="tab_class_1 container",
        style={'padding': '6px'}
    )


def create_tab2():
    table1 = pd.read_csv('inputTables/tab2/input1.csv')
    table2 = pd.read_csv('inputTables/tab2/input2.csv')
    return html.Div([
        html.H4('Engagement Details'),
        dt.DataTable(
            rows=table1.to_dict('records'),
            columns=table1.columns,
            id='table_1'
        ),
        html.H4('Engagement Analysis'),
        dt.DataTable(
            rows=table2.to_dict('records'),
            columns=table2.columns,
            id='table_2'
        ),
        html.Button('Download', id='button2', style={'margin-top': '10px'})
    ], id='tab_2',
        className="tab_class_2 container",
        style={'padding': '6px'}
    )


def create_tab3():
    table1 = pd.read_csv('inputTables/tab3/input1.csv')
    return html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
        ),
        html.H4('Population'),
        dt.DataTable(
            rows=table1.to_dict('records'),
            columns=table1.columns,
            id='table_1',
            editable=True,
            filterable=True,
            sortable=True,
            sortDirection="multi",
            row_selectable="multi",
            row_update=True
        ),
        html.Button('Download', id='button3', style={'margin-top': '10px'})
    ], id='tab_2',
        className="tab_class_3 container",
        style={'padding': '6px'}
    )


def create_tab4():
    table1 = pd.read_csv('inputTables/tab4/input1.csv')
    table2 = pd.read_csv('inputTables/tab4/input2.csv')
    return html.Div([
        html.H4('Control and Risk Details'),
        dt.DataTable(
            rows=table1.to_dict('records'),
            columns=table1.columns,
            id='table_1'
        ),
        html.H4('Population and Sample Procedures'),
        dt.DataTable(
            rows=table2.to_dict('records'),
            columns=table2.columns,
            id='table_2'
        ),
        html.H4('Test of Design Steps Performed'),
        dcc.Textarea(
            placeholder='Enter Data...',
            value='',
            style={'width': '100%'},
            id='table_3'
        ),
        html.H4('Test of Design Narrative'),
        dcc.Textarea(
            placeholder='Enter Data...',
            value='',
            style={'width': '100%'},
            id='table_4'
        ),
        html.H4('Test of Design Evidence'),
        dcc.Textarea(
            placeholder='Enter Data...',
            value='',
            style={'width': '100%'},
            id='table_5'
        ),
        html.H4('Test of Design Results'),
        dcc.Textarea(
            placeholder='Enter Data...',
            value='',
            style={'width': '100%'},
            id='table_6'
        ),
        html.Button('Download', id='button4', style={'margin-top': '10px'})
    ], id='tab_4',
        className="tab_class_4 container",
        style={'padding': '6px'}
    )


app.layout = html.Div([
        html.H2('Centralized Controls Monitoring and Testing (CCM) Operational'),
        dcc.Tabs(id='tabs', value=1, children=[
            dcc.Tab(label='Cover Page', value=1, style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Engagement Analysis', value=2, style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Population', value=3, style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Testing Details', value=4, style=tab_style, selected_style=tab_selected_style),
        ], style=tabs_styles),
        html.Div(id='tab-layout')
    ], id='app_layout',
        className='app_class')


# switching between tabs
@app.callback(dash.dependencies.Output('tab-layout', 'children'),
              [dash.dependencies.Input('tabs', 'value')])
def call_tab_layout(tab_value):
    if tab_value == 1:
        return create_tab1()
    if tab_value == 2:
        return create_tab2()
    if tab_value == 3:
        return create_tab3()
    if tab_value == 4:
        return create_tab4()


# dynamic select boxes creation 1
@app.callback(dash.dependencies.Output('select_next_1', 'children'),
              [dash.dependencies.Input('select_1', 'value')])
def call_select_1(value):
    print(value)
    if value == 'A':
        return [
            dcc.Dropdown(
                id='select_2',
                options=[
                    {'label': i, 'value': i} for i in ['A', 'B', 'C']
                ],
            ),
            html.Div([], id='select_next_2')
        ]


# dynamic select boxes creation 2
@app.callback(dash.dependencies.Output('select_next_2', 'children'),
              [dash.dependencies.Input('select_2', 'value')])
def call_select_2(value):
    print(value)
    if value == 'B':
        return [
            dcc.Dropdown(
                id='select_3',
                options=[
                    {'label': i, 'value': i} for i in ['A', 'B', 'C']
                ],
            ),
            html.Div([], id='select_next_3')
        ]


# dynamic select boxes creation 3
@app.callback(dash.dependencies.Output('select_next_3', 'children'),
              [dash.dependencies.Input('select_3', 'value')])
def call_select_3(value):
    print(value)
    if value == 'C':
        return [
            html.H4('Selected values A, B, C')
        ]


# Tab 1 table data fill
@app.callback(dash.dependencies.Output('table_1', 'rows'),
              [dash.dependencies.Input('select_3', 'value')])
def call_select_3(value):
    if value == 'C':
        return pd.read_csv('inputTables/tab1/input1_data.csv').to_dict('records')


# Tab 2 table data fill
@app.callback(dash.dependencies.Output('table_2', 'rows'),
              [dash.dependencies.Input('select_3', 'value')])
def call_select_3(value):
    if value == 'C':
        return pd.read_csv('inputTables/tab1/input2_data.csv').to_dict('records')


app.css.append_css({
    'external_url': 'static/css/dash.css'
})

if __name__ == '__main__':
    app.run_server(debug=True, port=8001)
