package tarea4.cl.tarea4.repository;

import tarea4.cl.tarea4.models.Actividad;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import java.util.List;

public interface ActividadRepository extends JpaRepository<Actividad, Long> {
    @Query("""
    SELECT a FROM Actividad a
    LEFT JOIN FETCH a.comuna c
    LEFT JOIN FETCH c.region
    WHERE a.termino IS NOT NULL
      AND a.termino <= CURRENT_TIMESTAMP
    """)
    List<Actividad> findFinalizadas();
}