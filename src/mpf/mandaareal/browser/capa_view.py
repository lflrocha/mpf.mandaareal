from Products.Five.browser import BrowserView
from plone import api

class CapaView(BrowserView):

    def noticias(self):
        brains = api.content.find(
            context=api.portal.get(),
            portal_type='News Item',
            review_state='published',
            sort_on='effective',
            sort_order='reverse',
        )

        resultado = []
        for brain in brains:
            url = brain.getURL()

            data_formatada = brain.effective.strftime('%d/%m/%y')
            resultado.append({
                'title': brain.Title,
                'description': brain.Description,
                'url': url,
                'date': data_formatada,
                'image': f"{url}/@@images/image/mini"
            })

        return resultado[:2]
