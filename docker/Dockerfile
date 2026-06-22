FROM odoo:19.0

LABEL org.opencontainers.image.title="odoo-self-hosted" \
      org.opencontainers.image.description="Self-hosted Odoo 19 learning environment" \
      org.opencontainers.image.source="https://github.com/isyll/odoo-self-hosted" \
      org.opencontainers.image.licenses="MIT"

USER root

RUN pip3 install --no-cache-dir --break-system-packages \
        debugpy \
        watchdog

USER odoo
