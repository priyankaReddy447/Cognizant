using Microsoft.EntityFrameworkCore;
using Module6_WebAPI.Models;
namespace Module6_WebAPI.Data;
public class ApplicationDbContext:DbContext{
 public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options):base(options){}
 public DbSet<Product> Products=>Set<Product>();
 protected override void OnModelCreating(ModelBuilder modelBuilder){
  modelBuilder.Entity<Product>().HasKey(p=>p.Id);
 }
}