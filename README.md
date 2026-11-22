# graphics_2d (v1.1.0)

2d graphics around turtle

## Usage Example

```python
import graphics_2d

window = graphics_2d.Window()
window.add_vertex(100, 50)
window.add_vertex(125, 25)
window.add_vertex(110, 75)
window.add_vertex(195, 80)
window.draw_dot(1)
window.draw_dot(2)
window.draw_dot(3)
window.draw_dot(4)
window.draw_quad(1, 2, 3, 4)
window.show()
```
1.0.0 functions:
- draw_dot()

### Changelog

changelog 1.0.1:
- added draw_line()

changelog 1.0.2:
- added draw_triangle()

changelog 1.1.0:
- remake system added vertices
- added add_vertex
- added draw_quad()
