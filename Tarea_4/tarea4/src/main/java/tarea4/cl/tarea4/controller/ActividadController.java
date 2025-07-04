package tarea4.cl.tarea4.controller;

import tarea4.cl.tarea4.models.ActividadDB;
import tarea4.cl.tarea4.service.ActividadService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api")
@CrossOrigin
public class ActividadController {

    private final ActividadService actividadService;

    public ActividadController(ActividadService actividadService) {
        this.actividadService = actividadService;
    }

    @GetMapping("/actividades/finalizadas")
    public List<ActividadDB> getActividadesFinalizadas() {
        return actividadService.obtenerActividadesFinalizadas();
    }

    @PostMapping("/notas")
    public ResponseEntity<Map<String, Object>> agregarNota(@RequestBody Map<String, String> body) {
        try {
            Integer actividadId = Integer.valueOf(body.get("actividadId"));
            Integer valorNota = Integer.valueOf(body.get("nota"));

            Double nuevoPromedio = actividadService.agregarNota(actividadId, valorNota);

            return ResponseEntity.ok(Map.of(
                    "nuevoPromedio", String.format("%.1f", nuevoPromedio)
            ));
        } catch (IllegalArgumentException ex) {
            return ResponseEntity.badRequest().body(Map.of("error", ex.getMessage()));
        }
    }
}