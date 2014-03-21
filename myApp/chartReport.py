
from report_tools.reports import Report
from report_tools.chart_data import ChartData
from report_tools.renderers.googlecharts import GoogleChartsRenderer
from report_tools import charts
from report_tools.renderers import ChartRenderer


class volumeHoraire (Report):

    renderer = GoogleChartsRenderer
    #renderer = ChartRenderer ()

    chart_DE = charts.ColumnChart(title="Volume ECTS  pour un Diplome", width="700", height=400)
    chart_DH = charts.ColumnChart(title="Volume Horaire  pour un Diplome", width="700", height=400)
    chart_YE_SI= charts.ColumnChart(title="Volume ECTS Sciences & Technologie  par Annee",width="700", height=400)
    chart_YH_SI= charts.ColumnChart(title="Volume Horaire Sciences & Technologie  par Annee",width="700", height=400)
    chart_YE_EG= charts.ColumnChart(title="Volume ECTS Economie et Gestion par Annee",width="700", height=400)
    chart_YH_EG= charts.ColumnChart(title="Volume Horaire Economie et Gestion par Annee",width="700", height=400)

    ##chart_DE
    D_EG_E=[]
    D_SI_E=[]
    ##chart_DH
    D_EG_H=[]
    D_SI_H=[]
    ##chart_YE_SI
    s1_Y_SI_E=[]
    s2_Y_SI_E=[]
    ##chart_YH_SI
    s1_Y_SI_H=[]
    s2_Y_SI_H=[]
    ##chart_YE_EG
    s1_Y_EG_E=[]
    s2_Y_EG_E=[]
    ##chart_YH_EG
    s1_Y_EG_H=[]
    s2_Y_EG_H=[]



    def get_data_for_chart_DE(self):
        data = ChartData()

        data.add_column("ETCS")
        data.add_column("Licence")
        data.add_column("Master")


        data.add_row(self.D_SI_E)
        data.add_row(self.D_EG_E)

        #data.add_row(["s1",10, 18, 20,22,21,24])
        #data.add_row(["s2",10, 18, 20,22,21,24])

        return data
    def get_data_for_chart_DH(self):
        data = ChartData()

        data.add_column("Horaire")
        data.add_column("Licence")
        data.add_column("Master")


        data.add_row(self.D_SI_H)
        data.add_row(self.D_EG_H)

        #data.add_row(["s1",10, 18, 20,22,21,24])
        #data.add_row(["s2",10, 18, 20,22,21,24])

        return data


    def get_data_for_chart_YE_SI(self):
        data = ChartData()

        data.add_column("ETCS")
        data.add_column("Prep")
        data.add_column("L1")
        data.add_column("L2")
        data.add_column("L3")
        data.add_column("M1")
        data.add_column("M2")

        data.add_row(self.s1_Y_SI_E)
        data.add_row(self.s2_Y_SI_E)

        #data.add_row(["s1",10, 18, 20,22,21,24])
        #data.add_row(["s2",10, 18, 20,22,21,24])

        return data


    def get_data_for_chart_YH_SI(self):
        data = ChartData()

        data.add_column("Horaire")
        data.add_column("Prep")
        data.add_column("L1")
        data.add_column("L2")
        data.add_column("L3")
        data.add_column("M1")
        data.add_column("M2")

        data.add_row(self.s1_Y_SI_H)
        data.add_row(self.s2_Y_SI_H)

        #data.add_row(["s1",10, 18, 20,22,21,24])
        #data.add_row(["s2",10, 18, 20,22,21,24])

        return data
    def get_data_for_chart_YE_EG(self):
        data = ChartData()

        data.add_column("ETCS")
        data.add_column("L1")
        data.add_column("L2")
        data.add_column("L3")
        data.add_column("M1")
        data.add_column("M2")

        data.add_row(self.s1_Y_EG_E)
        data.add_row(self.s2_Y_EG_E)

        #data.add_row(["s1",10, 18, 20,22,21,24])
        #data.add_row(["s2",10, 18, 20,22,21,24])

        return data
    def get_data_for_chart_YH_EG(self):
        data = ChartData()

        data.add_column("Horaire")
        data.add_column("L1")
        data.add_column("L2")
        data.add_column("L3")
        data.add_column("M1")
        data.add_column("M2")

        data.add_row(self.s1_Y_EG_H)
        data.add_row(self.s2_Y_EG_H)

        #data.add_row(["s1",10, 18, 20,22,21,24])
        #data.add_row(["s2",10, 18, 20,22,21,24])

        return data
