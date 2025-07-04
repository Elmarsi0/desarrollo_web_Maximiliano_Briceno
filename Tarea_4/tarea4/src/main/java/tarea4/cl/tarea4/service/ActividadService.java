package tarea4.cl.tarea4.service;

import tarea4.cl.tarea4.models.ActividadDB;
import tarea4.cl.tarea4.models.Actividad;
import tarea4.cl.tarea4.models.Nota;
import tarea4.cl.tarea4.repository.ActividadRepository;
import tarea4.cl.tarea4.repository.NotaRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ActividadService {

    private final ActividadRepository actividadRepository;
    private final NotaRepository notaRepository;

    public ActividadService(ActividadRepository actividadRepository, NotaRepository notaRepository) {
        this.actividadRepository = actividadRepository;
        this.notaRepository = notaRepository;
    }

    @Transactional(readOnly = true)
    public List<ActividadDB> obtenerActividadesFinalizadas() {
        return actividadRepository.findFinalizadas().stream()
    .map(actividad -> {
        Double promedio = notaRepository.findPromedioByActividadId(actividad.getId());
        String notaPromedio = (promedio == null) ? "-" : String.format("%.1f", promedio);
        return new ActividadDB(
            actividad.getId(),
            actividad.getNombre(),
            actividad.getTema(),
            actividad.getInicio() != null ? actividad.getInicio().toLocalDate() : null,
            actividad.getTermino() != null ? actividad.getTermino().toLocalDate() : null,
            // Extraer nombre de la región (String), si región es un objeto
            actividad.getRegion() != null ? actividad.getRegion().getNombre() : null,
            // Extraer nombre de comuna (String)
            actividad.getComuna() != null ? actividad.getComuna().getNombre() : null,
            actividad.getSector(),
            actividad.getFoto(),
            notaPromedio
        );
    }).collect(Collectors.toList());
}

    @Transactional
    public Double agregarNota(Integer actividadId, Integer valorNota) {
        if (valorNota < 1 || valorNota > 7) {
            throw new IllegalArgumentException("Nota fuera de rango (1-7)");
        }

        Actividad actividad = actividadRepository.findById(actividadId.longValue())
                .orElseThrow(() -> new IllegalArgumentException("Actividad no encontrada"));

        Nota nota = new Nota();
        nota.setActividad(actividad);
        nota.setNota(valorNota);
        notaRepository.save(nota);

        return notaRepository.findPromedioByActividadId(actividadId);
    }
}
