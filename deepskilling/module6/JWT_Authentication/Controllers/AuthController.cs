using Microsoft.AspNetCore.Mvc;
namespace Demo.Controllers;
[ApiController]
[Route("api/[controller]")]
public class AuthController:ControllerBase{
 [HttpPost("login")]
 public IActionResult Login()=>Ok(new{token="sample-jwt-token"});
}