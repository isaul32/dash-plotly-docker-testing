FROM r-base:4.2.1
RUN apt-get update && apt-get install -y \
    libfontconfig1-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libfreetype6-dev \
    libpng-dev \
    libtiff5-dev \
    libjpeg-dev \
    libxml2-dev \
    libgit2-dev \
    curl \
    libcurl4-openssl-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/local/src/dashr
RUN Rscript -e 'install.packages(c("fiery", "routr", "reqres", "htmltools", "base64enc", "plotly", "mime", "crayon", "devtools"), repos = "https://cloud.r-project.org")'
RUN Rscript -e 'devtools::install_github("plotly/dashR", ref = "dev", upgrade = TRUE)'
COPY . .
ENV DASH_HOST=::
ENV DASH_PORT=8000
EXPOSE 8000
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1
CMD ["Rscript", "app.R"]
