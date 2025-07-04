package tarea4.cl.tarea4.models;

import java.time.LocalDate;

public class ActividadDB {
    private Integer id;
    private String nombre;
    private String tema;
    private LocalDate inicio;
    private LocalDate termino;
    private String region;
    private String comuna;
    private String sector;
    private String foto;
    private String notaPromedio;

    public ActividadDB() {}

    public ActividadDB(Integer id, String nombre, String tema,
                        LocalDate inicio, LocalDate termino,
                        String region, String comuna, String sector,
                        String foto, String notaPromedio) {
        this.id = id;
        this.nombre = nombre;
        this.tema = tema;
        this.inicio = inicio;
        this.termino = termino;
        this.region = region;
        this.comuna = comuna;
        this.sector = sector;
        this.foto = foto;
        this.notaPromedio = notaPromedio;
    }

    // Getters y Setters
    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    public String getTema() { return tema; }
    public void setTema(String tema) { this.tema = tema; }
    public LocalDate getInicio() { return inicio; }
    public void setInicio(LocalDate inicio) { this.inicio = inicio; }
    public LocalDate getTermino() { return termino; }
    public void setTermino(LocalDate termino) { this.termino = termino; }
    public String getRegion() { return region; }
    public void setRegion(String region) { this.region = region; }
    public String getComuna() { return comuna; }
    public void setComuna(String comuna) { this.comuna = comuna; }
    public String getSector() { return sector; }
    public void setSector(String sector) { this.sector = sector; }
    public String getFoto() { return foto; }
    public void setFoto(String foto) { this.foto = foto; }
    public String getNotaPromedio() { return notaPromedio; }
    public void setNotaPromedio(String notaPromedio) { this.notaPromedio = notaPromedio; }
}
