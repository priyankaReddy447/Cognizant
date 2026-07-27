using Microsoft.AspNetCore.Mvc;
namespace Demo.Controllers;
[ApiController]
[Route("api/[controller]")]
public class ProductsController:ControllerBase{
 [HttpGet] public IActionResult Get()=>Ok(new[]{"Product1","Product2"});
}